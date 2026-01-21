from django.urls import path
from . import views


app_name = 'salon'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/salons/', views.salon_list_api, name='salon_list_api'),
]