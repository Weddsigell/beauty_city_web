import random
from django.shortcuts import render
from django.utils import timezone


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Client


@csrf_exempt
def get_or_create_client(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        phone = data.get('phone')
        name = data.get('name', '')
        
        if not phone:
            return JsonResponse({'error': 'Phone is required'}, status=400)
        
        client, created = Client.objects.get_or_create(
            phone=phone,
            defaults={'name': name}
        )
        
        return JsonResponse({
            'id': client.id,
            'name': client.name,
            'phone': client.phone,
            'created': created,
        })
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)


def client_detail_api(request, client_id):
    try:
        client = Client.objects.get(id=client_id)
        return JsonResponse({
            'id': client.id,
            'name': client.name,
            'phone': client.phone,
        })
    except Client.DoesNotExist:
        
        return JsonResponse({'error': 'Client not found'}, status=404)
    

@csrf_exempt
def send_sms_code(request):
    """Отправить SMS-код (заглушка)"""
    if request.method == 'POST':
        data = json.loads(request.body)
        phone = data.get('phone')
        
        if not phone:
            return JsonResponse({'error': 'Phone required'}, status=400)
        

        client, _ = Client.objects.get_or_create(phone=phone)
        
        code = str(random.randint(1000, 9999))
        client.sms_code = code
        client.code_created_at = timezone.now()
        client.save()
        
        # заглушка SMS
        print(f"📱 SMS для {phone}: код {code}")
        
        return JsonResponse({
            'success': True,
            'message': 'Code sent',
            'debug_code': code,
        })
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
        
        
@csrf_exempt
def verify_sms_code(request):
    """Проверить SMS-код"""
    if request.method == 'POST':
        data = json.loads(request.body)
        phone = data.get('phone')
        code = data.get('code')
        
        try:
            client = Client.objects.get(phone=phone)
        except Client.DoesNotExist:
            return JsonResponse({'error': 'Client not found'}, status=404)
        
        if client.sms_code == code:
            request.session['client_id'] = client.id
            client.sms_code = '' 
            client.save()
            return JsonResponse({'success': True, 'client_id': client.id})
        
        return JsonResponse({'error': 'Invalid code'}, status=400)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)