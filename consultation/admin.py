from django.contrib import admin

from .models import Consultation


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "created_at", "status")
    list_display_links = ("name", "phone", "created_at", "status")
