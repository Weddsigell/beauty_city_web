from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Salon


@login_required
def render_salons(request):
    context = {
        "salons": Salon.objects.all(),
    }

    return render(request, "salons.html", context=context)
