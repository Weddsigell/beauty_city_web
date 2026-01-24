from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

from .models import Master, ScheduleMaster, Specialization


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "photo_preview",
        "experience_months",
    )
    list_display_links = ("name",)
    readonly_fields = ("photo_preview",)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="80" style="border-radius: 8px;" />',
                obj.photo.url,
            )
        return "-"

    photo_preview.short_description = "Фото"

    def experience_months(self, obj):
        delta = timezone.now().date() - obj.start_work
        return delta.days // 30

    experience_months.short_description = "Стаж(мес)"


class MasterInline(admin.TabularInline):
    model = Specialization.masters.through
    extra = 0
    verbose_name = "Мастер"
    verbose_name_plural = "Мастера"


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("name", "masters_count")
    list_display_links = ("name",)
    inlines = [MasterInline]
    exclude = ("masters",)

    def masters_count(self, obj):
        return obj.masters.count()

    masters_count.short_description = "Кол-во мастеров"


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
