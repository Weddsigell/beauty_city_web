from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        user = self.model(phone=phone, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(phone=phone, password=password, **extra_fields)


class User(AbstractUser):
    username = None
    email = None

    is_staff = models.BooleanField(default=False, verbose_name="Админ")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    is_superuser = models.BooleanField(default=False, verbose_name="Суперпользователь")

    name = models.CharField(max_length=255, verbose_name="Имя", default="")
    phone = models.CharField(
        unique=True,
        verbose_name="Телефон",
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                r"^\+79\d{9}$", message="Номер должен быть в формате +7XXXXXXXXXX"
            ),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.phone} - {self.name}"
