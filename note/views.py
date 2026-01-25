from datetime import datetime, timedelta
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone

from master.models import Master
from procedure.models import Category, Procedure
from salon.models import Salon
from user.services import register_or_login
from django.db.models import Q
from .models import Note


def get_free_slots_with_busy(master, days_ahead=14):
    """
    Возвращает свободные слоты, исключая занятые записи.
    Использует interval из ScheduleMaster.
    """
    today = timezone.now().date()
    result = {}

    for i in range(days_ahead):
        current_date = today + timedelta(days=i)
        date_str = current_date.strftime("%d.%m.%Y")

        weekday = current_date.weekday()

        schedule = master.schedules.filter(day=weekday, is_active=True).first()

        if not schedule:
            continue

        start_dt = datetime.combine(current_date, schedule.start_time)
        end_dt = datetime.combine(current_date, schedule.end_time)
        interval = schedule.interval  # ← берём из модели

        slots = []
        current = start_dt
        while current + timedelta(minutes=interval) <= end_dt:
            slot_time = current.time()
            slot_end_time = (current + timedelta(minutes=interval)).time()

            # Проверяем, есть ли пересекающаяся запись
            is_busy = Note.objects.filter(
                master=master,
                date=current_date,
                time__lt=slot_end_time,
                time__gte=slot_time,
            ).exists()

            if not is_busy:
                slots.append(current.strftime("%H:%M"))

            current += timedelta(minutes=interval)

        if slots:
            result[date_str] = slots

    return result


def upcoming_notes_by_user(id):
    date_now = timezone.now().date()
    time_now = timezone.now().time()
    try:
        return Note.objects.filter(user=id).filter(Q(date__gt=date_now) | Q(date=date_now, time__gte=time_now))
    except Exception as e:
        raise e


def past_notes_by_user(id):
    date_now = timezone.now().date()
    time_now = timezone.now().time()
    print(Note.objects.filter(user=id).filter(Q(date__lt=date_now) | Q(date=date_now, time__lte=time_now)))
    try:
        return Note.objects.filter(user=id).filter(Q(date__lt=date_now) | Q(date=date_now, time__lte=time_now))
    except Exception as e:
        raise e


@login_required
def render_notes(request):
    past_notes = past_notes_by_user(id=request.user.id)
    upcoming_notes = upcoming_notes_by_user(id=request.user.id)
    context = {
        "past_notes": past_notes,
        "upcoming_notes": upcoming_notes,
        "has_past_notes": past_notes.exists(),
        "has_upcoming_notes": upcoming_notes.exists(),
        "sum": sum([note.procedure.price for note in upcoming_notes]),
    }

    return render(request, "notes.html", context=context)


def render_categories(request):
    context = {
        "categories": Category.objects.all(),
    }

    return render(request, "procedures.html", context=context)


def render_masters(request):
    request.session["salon"] = request.POST.get("salon_id", None)
    context = {
        "masters": Master.objects.filter(
            procedures=int(request.session["procedure"]),
            salon=int(request.session["salon"]),
        ),
    }

    return render(request, "masters.html", context=context)


def render_salons(request):
    request.session["procedure"] = request.POST.get("procedure_id", None)
    masters = Master.objects.filter(procedures=int(request.session["procedure"]))
    print(masters)
    context = {
        "salons": Salon.objects.filter(masters__in=masters),
    }

    return render(request, "salons.html", context=context)


def render_date(request):
    request.session["master"] = request.POST.get("master_id", None)
    master = Master.objects.get(id=int(request.session["master"]))
    datetime = get_free_slots_with_busy(master, days_ahead=14)

    context = {
        "free_slots": datetime,
    }

    return render(request, "date.html", context=context)


def render_record_finaly(request):
    date = request.POST.get("selected_slot", None)
    request.session["date"] = date
    procedure = Procedure.objects.get(id=int(request.session["procedure"]))
    context = {
        "master": Master.objects.get(id=int(request.session["master"])),
        "procedure": procedure,
        "salon": Salon.objects.get(id=int(request.session["salon"])),
        "date": date,
        "price": procedure.price,
    }
    return render(request, "record_finaly.html", context=context)


def create_note(request):
    user = register_or_login(request, request.POST["phone"])
    if not user:
        return render(request, "index.html")
    user.name = request.POST["name"]
    user.save()

    try:
        master = Master.objects.get(id=int(request.session["master"]))
        procedure = Procedure.objects.get(id=int(request.session["procedure"]))

        date = request.session.get("date")
        dt = datetime.strptime(date, "%d.%m.%Y %H:%M")
        date_part = dt.strftime("%Y-%m-%d")
        time_part = dt.strftime("%H:%M")

        note = Note.objects.create(
            user=user,
            master=master,
            procedure=procedure,
            price=procedure.price,
            date=date_part,
            time=time_part,
        )
    except Exception as e:
        print(e)
        messages.error(request, "Что-то пошло не так, попробуйте позже!")
        return render(request, "index.html")

    return redirect("notes_page")
