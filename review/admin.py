from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "text", "created_at", "grade")
    list_display_links = ("user", "text", "created_at")
