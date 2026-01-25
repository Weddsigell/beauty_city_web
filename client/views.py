import json
import random
from datetime import timedelta

from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Client


def generate_code():
    return str(random.randint(1000, 9999))


@csrf_exempt
@require_POST
def send_sms_code(request):
    try:
        data = json.loads(request.body)
        phone = data.get("phone", "").strip()

        if not phone:
            return JsonResponse({"success": False, "error": "Укажите телефон"})

        # Нормализуем телефон (убираем +, пробелы, скобки, тире)
        phone = "".join(c for c in phone if c.isdigit())
        if phone.startswith("8"):
            phone = "7" + phone[1:]

        # Создаём или получаем клиента
        client, created = Client.objects.get_or_create(phone=phone)

        # Генерируем код
        code = generate_code()
        client.sms_code = code
        client.code_created_at = timezone.now()
        client.save()

        # В реальном проекте здесь отправка SMS
        # Для разработки выводим код в консоль
        print(f"SMS код для {phone}: {code}")

        return JsonResponse({"success": True})

    except json.JSONDecodeError:
        return JsonResponse({"success": False, "error": "Неверный формат данных"})


@csrf_exempt
@require_POST
def verify_sms_code(request):
    try:
        data = json.loads(request.body)
        phone = data.get("phone", "").strip()
        code = data.get("code", "").strip()

        if not phone or not code:
            return JsonResponse({"success": False, "error": "Укажите телефон и код"})

        # Нормализуем телефон
        phone = "".join(c for c in phone if c.isdigit())
        if phone.startswith("8"):
            phone = "7" + phone[1:]

        try:
            client = Client.objects.get(phone=phone)
        except Client.DoesNotExist:
            return JsonResponse({"success": False, "error": "Клиент не найден"})

        # Проверяем код
        if client.sms_code != code:
            return JsonResponse({"success": False, "error": "Неверный код"})

        # Проверяем срок действия кода (5 минут)
        if client.code_created_at:
            code_age = timezone.now() - client.code_created_at
            if code_age > timedelta(minutes=5):
                return JsonResponse({"success": False, "error": "Код истёк"})

        # Очищаем код
        client.sms_code = ""
        client.code_created_at = None
        client.save()

        # Сохраняем в сессии
        request.session["client_id"] = client.id
        request.session["client_phone"] = client.phone

        return JsonResponse({"success": True, "client_id": client.id})

    except json.JSONDecodeError:
        return JsonResponse({"success": False, "error": "Неверный формат данных"})
