from django.contrib import admin

from .models import Note


@admin.register(Note)
class NotetAdmin(admin.ModelAdmin):
    list_display = [
        "client",
        "procedure",
        "master",
        "price",
        "date",
        "time",
        "created_at",
    ]
    list_display_links = [
        "client",
        "procedure",
    ]
