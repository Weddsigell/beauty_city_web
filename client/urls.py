from django.urls import path
from . import views


app_name = 'client'

urlpatterns = [
    path('api/client/', views.get_or_create_client, name='get_or_create'),
    path('api/client/<int:client_id>/', views.client_detail_api, name='detail'),
    path('api/auth/send-code/', views.send_sms_code, name='send_sms_code'),
    path('api/auth/verify/', views.verify_sms_code, name='verify_sms_code'),
]