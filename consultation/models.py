from django.db import models


class Consultation(models.Model):
    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="consultations",
    )
    question = models.TextField(verbose_name="Вопрос", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(
        verbose_name="Статус",
        choices=[(0, "Новый"), (1, "В обработке"), (2, "Закрыт")],
        default=0,
    )

    def __str__(self):
        return f"{self.user.name} {self.created_at} {self.status}"
