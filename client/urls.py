from django.urls import path

from . import views

urlpatterns = [
    path("api/auth/send-code/", views.send_sms_code, name="send_sms_code"),
    path("api/auth/verify/", views.verify_sms_code, name="verify_sms_code"),
]
