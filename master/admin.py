from django.contrib import admin
from django.utils.html import format_html

from .models import Master, ScheduleMaster, Specialization


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "photo_preview",
        "get_experience",
    )
    list_display_links = ("name",)
    readonly_fields = ("photo_preview",)

    @admin.display(description="Фото")
    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="80" style="border-radius: 8px;" />',
                obj.photo.url,
            )
        return "-"

    @admin.display(description="Стаж (мес.)")
    def get_experience(self, obj):
        return obj.experience



@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("name", "masters_count")
    list_display_links = ("name",)
    exclude = ("masters",)

    @admin.display(description="Кол-во мастеров")
    def masters_count(self, obj):
        return obj.masters.count()


@admin.register(ScheduleMaster)
class ScheduleMasterAdmin(admin.ModelAdmin):
    list_display = (
        "master",
        "day",
        "is_active",
        "start_time",
        "end_time",
        "interval",
    )
    list_display_links = ("master", "day")
