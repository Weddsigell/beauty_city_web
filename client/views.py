from django.shortcuts import render


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