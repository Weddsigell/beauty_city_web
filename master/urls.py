from django.urls import path
from . import views

urlpatterns = [
    path("masters/", views.render_masters, name="masters_page"),
]