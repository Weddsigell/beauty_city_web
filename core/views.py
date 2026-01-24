from django.shortcuts import render

from master.models import Master
from procedure.models import Procedure
from review.models import Review
from salon.models import Salon


def render_index(request):
    context = {
        "salons": Salon.objects.all(),
        "procedures": Procedure.objects.all(),
        "masters": Master.objects.all(),
        "reviews": Review.objects.all(),
    }
    return render(request, "index.html", context=context)
