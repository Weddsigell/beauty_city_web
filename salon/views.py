from django.shortcuts import render

from .models import Salon


def render_salons(request):
    context = {
        "salons": Salon.objects.all(),
    }

    return render(request, "salons.html", context=context)
