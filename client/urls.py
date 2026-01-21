from django.urls import path
from . import views


app_name = 'client'

urlpatterns = [
    path('api/client/', views.get_or_create_client, name='get_or_create'),
    path('api/client/<int:client_id>/', views.client_detail_api, name='detail'),
]