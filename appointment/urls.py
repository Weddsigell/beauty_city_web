from django.urls import path

from .views import render_notes

urlpatterns = [
    path("notes/<int:client_id>/", render_notes, name="notes_page"),
]
