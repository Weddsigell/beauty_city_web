from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["phone", "name", "code_created_at"]
    search_fields = ["phone", "name"]
