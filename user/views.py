from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .services import register_or_login


@require_http_methods("POST")
def auth(request):
    phone = request.POST.get("phone", None)

    user = register_or_login(request, phone)
    if not user:
        return render(request, "index.html")

    return redirect("index_page")
