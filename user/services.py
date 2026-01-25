from django.contrib import messages
from django.contrib.auth import login
from django.core.exceptions import ValidationError

from .models import User


def register_or_login(request, phone):
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
        user, created = User.objects.get_or_create(phone=phone)

        if created:
            user.set_unusable_password()
            user.save()
    except ValidationError:
        messages.error(request, "Ошибка при создании пользователя!")
        return None
    except Exception:
        messages.error(request, "Что-то пошло не так, попробуйте позже!")
        return None

    login(request, user)

    return user
