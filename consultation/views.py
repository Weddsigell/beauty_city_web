from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

from .models import Consultation


def create_consultation(request, phone, name, question):
    if not name:
        messages.error(request, "Имя обязательно!")
        return None

    if not phone:
        messages.error(request, "Телефон обязателен!")
        return None

    phone = phone.strip()

    if not phone.startswith("79"):
        messages.error(request, "Неккоректный телефон!")
        return None

    if len(str(phone)) != 11:
        messages.error(request, "Неккоректный телефон!")
        return None

    try:
        consultation, created = Consultation.objects.get_or_create(
            phone=phone, name=name, question=question
        )
    except ValidationError:
        messages.error(request, "Ошибка при создании заявки!")
        return None
    except Exception:
        messages.error(request, "Что-то пошло не так, попробуйте позже!")
        return None

    return consultation


@require_http_methods("POST")
def consultation(request):
    phone = request.POST.get("phone", None)
    name = request.POST.get("name", None)
    question = request.POST.get("question", None)

    consultation = create_consultation(request, phone, name, question)

    if not consultation:
        return redirect("index_page")

    return redirect("index_page")
