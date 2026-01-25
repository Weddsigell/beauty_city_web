from django.urls import path

from . import views

urlpatterns = [
    path("", views.render_index, name="index_page"),
    path("admin2/", views.render_admin, name="admin2_page"),
]
