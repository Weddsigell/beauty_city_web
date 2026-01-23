from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("phone", "name", "is_staff")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = "__all__"


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = (
        "phone",
        "name",
        "created_at",
        "is_staff",
        "is_active",
        "is_superuser",
    )
    list_display_links = ("phone", "name")
    search_fields = ("phone__raw", "name")
    list_filter = ("is_staff", "is_superuser", "is_active")
    ordering = ["created_at"]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone",
                    "name",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "password",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone",
                    "name",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "password1",
                    "password2",
                )
            },
        ),
    )
