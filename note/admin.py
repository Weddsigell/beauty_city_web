from django.contrib import admin

from .models import Note


@admin.register(Note)
class NotetAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "procedure",
        "master",
        "price",
        "date",
        "time",
        "created_at",
    ]
    list_display_links = [
        "user",
        "procedure",
    ]
