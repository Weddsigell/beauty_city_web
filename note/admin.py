from django.contrib import admin

from .models import Note


@admin.register(Note)
class NotetAdmin(admin.ModelAdmin):
    list_display = [
        "client",
        "master",
        "service",
        "price",
        "date",
        "time",
        "created_at",
    ]
