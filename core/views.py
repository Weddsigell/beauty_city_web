from django.shortcuts import render

from master.models import Master
from procedure.models import Procedure
from review.models import Review
from salon.models import Salon


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
