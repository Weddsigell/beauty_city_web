from django.db import models


class Client(models.Model):
    phone = models.CharField(max_length=20, unique=True, verbose_name="Телефон")
    name = models.CharField(max_length=100, blank=True, verbose_name="Имя")
    sms_code = models.CharField(max_length=6, blank=True, verbose_name="SMS-код")
    code_created_at = models.DateTimeField(
        blank=True, null=True, verbose_name="Код создан"
    )

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.name} ({self.phone})"
