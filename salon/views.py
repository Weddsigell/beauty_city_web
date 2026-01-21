from django.shortcuts import render


from django.shortcuts import render
from django.http import JsonResponse
from .models import Salon


def index(request):
    salons = Salon.objects.all()
    
    return render(request, 'index.html', {'salons': salons})


def salon_list_api(request):
    salons = Salon.objects.all()
    data = [
        {
            'id': salon.id,
            'title': salon.title,
            'address': salon.address,
            'phone': salon.phone,
            'image': salon.image.url if salon.image else None,
        }
        for salon in salons
    ]
    
    return JsonResponse(data, safe=False)