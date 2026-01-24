from django.urls import path

from .views import (
    render_masters,
    render_notes,
    render_procedures,
    render_record_finaly,
    render_salons,
)

urlpatterns = [
    path("notes/", render_notes, name="notes_page"),
    path("procedures/", render_procedures, name="procedures_page"),
    path("masters/", render_masters, name="masters_page"),
    path("salons/", render_salons, name="salons_page"),
    path("record_finaly/", render_record_finaly, name="record_finaly_page"),
]
