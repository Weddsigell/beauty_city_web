from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Procedure


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "photo_preview"]
    list_display_links = [
        "name",
    ]
    readonly_fields = ("photo_preview",)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="80" style="border-radius: 8px;" />',
                obj.photo.url,
            )
        return "-"

    photo_preview.short_description = "Фото"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
