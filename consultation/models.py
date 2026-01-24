from django.core.validators import RegexValidator
from django.db import models


class Consultation(models.Model):
    name = models.CharField(
        verbose_name="Имя",
    )
    question = models.TextField(verbose_name="Вопрос", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(
        verbose_name="Статус",
        choices=[(0, "Новый"), (1, "В обработке"), (2, "Закрыт")],
        default=0,
    )
    phone = models.CharField(
        verbose_name="Телефон",
        validators=[
            RegexValidator(
                r"^79\d{9}$", message="Номер должен быть в формате +7XXXXXXXXXX"
            ),
        ],
    )

    def __str__(self):
        return f"{self.name} {self.created_at} {self.status}"
