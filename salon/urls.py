from django.urls import path

from . import views

urlpatterns = [
    path("salons/", views.render_salons, name="salons_page"),
]
