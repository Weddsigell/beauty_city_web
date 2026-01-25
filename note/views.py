from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone

from master.models import Master
from procedure.models import Category, Procedure
from salon.models import Salon

from .models import Note


def upcoming_notes_by_client(id):
    date_now = timezone.now().date()
    time_now = timezone.now().time()
    print(date_now, time_now)
    print(Note.objects.get(id=1))
    try:
        return Note.objects.filter(client=id, date__gte=date_now, time__gte=time_now)
    except Exception as e:
        raise e


def past_notes_by_client(id):
    date_now = timezone.now().date()
    time_now = timezone.now().time()
    try:
        return Note.objects.filter(client=id, date__lt=date_now, time__lt=time_now)
    except Exception as e:
        raise e


@login_required
def render_notes(request):
    past_notes = past_notes_by_client(id=request.user.id)
    upcoming_notes = upcoming_notes_by_client(id=request.user.id)
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
    context = {
        "masters": Master.objects.all(),
    }

    return render(request, "masters.html", context=context)


def render_salons(request):
    context = {
        "salons": Salon.objects.all(),
    }

    return render(request, "salons.html", context=context)


def render_time(request):
    context = {}

    return render(request, "time.html", context=context)


def render_record_finaly(request):
    procedure = Procedure.objects.get(id=1)
    context = {
        "master": Master.objects.get(id=1),
        "procedure": procedure,
        "salon": Salon.objects.get(id=1),
        "date": "11",
        "time": "10:00",
        "price": procedure.price,
    }
    return render(request, "record_finaly.html", context=context)


def create_note(request):
    return redirect("notes_page")
