from django.urls import path
from . import views

urlpatterns = [
    path("procedures/", views.render_procedures, name="procedures_page"),
]