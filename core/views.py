from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from master.models import Master
from note.models import Note
from procedure.models import Procedure
from review.models import Review
from salon.models import Salon
from user.models import User


def render_index(request):
    salons = Salon.objects.all()

    # Данные для Яндекс Карты
    salons_json = [
        {
            "name": salon.name,
            "address": salon.address,
            "lat": float(salon.latitude) if salon.latitude else None,
            "lng": float(salon.longitude) if salon.longitude else None,
        }
        for salon in salons
    ]

    context = {
        "salons": salons,
        "salons_json": salons_json,
        "procedures": Procedure.objects.all(),
        "masters": Master.objects.all(),
        "reviews": Review.objects.all(),
    }
    return render(request, "index.html", context=context)


def sum_mounth():
    note_mounth = Note.objects.filter(
        created_at__gte=(timezone.now() - timezone.timedelta(days=30)),
        payment_status=True,
    )
    sum = 0
    try:
        for note in note_mounth:
            sum += note.price

        return sum
    except Exception:
        return sum


@login_required
def render_admin(request):
    user_mounth = User.objects.filter(
        created_at__gte=(timezone.now() - timezone.timedelta(days=30))
    ).count()
    note_mounth = Note.objects.filter(
        created_at__gte=(timezone.now() - timezone.timedelta(days=30)),
        payment_status=True,
    ).count()
    user_year = User.objects.filter(
        created_at__gte=(timezone.now() - timezone.timedelta(days=365))
    ).count()
    percent = (note_mounth / user_mounth) * 100

    context = {
        "user": User.objects.get(id=request.user.id, is_superuser=True),
        "user_mounth": user_mounth,
        "user_year": user_year,
        "percent_mounth": percent,
        "sum_mounth": sum_mounth(),
    }

    return render(request, "admin.html", context=context)
