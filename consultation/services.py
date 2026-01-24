from django.contrib import messages
from django.core.exceptions import ValidationError

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
