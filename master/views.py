from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Master


@login_required
def render_masters(request):
    context = {
        "masters": Master.objects.all(),
    }

    return render(request, "masters.html", context=context)
