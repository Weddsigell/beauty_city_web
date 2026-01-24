from django.contrib import admin

from .models import Consultation


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "status")
    list_display_links = ("user", "created_at", "status")
