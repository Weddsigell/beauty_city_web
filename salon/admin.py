from django.contrib import admin
from django.utils.html import format_html

from .models import Salon, ScheduleSalon


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "photo_preview"]
    list_display_links = ["name", "address"]
    readonly_fields = ("photo_preview",)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="80" style="border-radius: 8px;" />',
                obj.photo.url,
            )
        return "-"

    photo_preview.short_description = "Фото"


@admin.register(ScheduleSalon)
class ScheduleSalonAdmin(admin.ModelAdmin):
    list_display = (
        "salon",
        "day",
        "is_active",
        "start_time",
        "end_time",
    )
    list_display_links = ("salon", "day")
