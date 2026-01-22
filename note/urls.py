from django.urls import path

from .views import render_notes

urlpatterns = [
    path("notes/", render_notes, name="notes_page"),
    path("service/", render_notes, name="service_page"),
]
