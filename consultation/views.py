from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

from .services import create_consultation


@require_http_methods("POST")
def consultation(request):
    phone = request.POST.get("phone", None)
    name = request.POST.get("name", None)
    question = request.POST.get("question", None)

    consultation = create_consultation(request, phone, name, question)

    if not consultation:
        return redirect("index_page")

    return redirect("index_page")
