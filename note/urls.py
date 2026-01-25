from django.urls import path

from . import views

urlpatterns = [
    path("notes/", views.render_notes, name="notes_page"),
    path("procedures/", views.render_categories, name="procedures_page"),
    path("masters/", views.render_masters, name="masters_page"),
    path("salons/", views.render_salons, name="salons_page"),
    path("record_finaly/", views.render_record_finaly, name="record_finaly_page"),
    path("create_note/", views.create_note, name="create_note"),
]
