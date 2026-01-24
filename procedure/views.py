from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from procedure.models import Category


@login_required
def render_procedures(request):
    context = {"categories": Category.objects.all()}

    return render(request, "procedures.html", context=context)
