from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.render_index, name="index_page"),
]
