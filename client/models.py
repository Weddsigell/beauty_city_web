from django.db import models


class Client(models.Model):
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=20, unique=True)
    sms_code = models.CharField("SMS-код", max_length=6, blank=True)
    code_created_at = models.DateTimeField("Код создан", null=True, blank=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.name} ({self.phone})"
