from django.db import models


class Note(models.Model):
    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, verbose_name="Клиент", related_name="notes"
    )
    master = models.ForeignKey(
        "master.Master",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Мастер",
        related_name="notes",
    )
    procedure = models.ForeignKey(
        "procedure.Procedure",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Услуга",
        related_name="notes",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    date = models.DateField(verbose_name="Дата записи")
    time = models.TimeField(verbose_name="Время записи")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания записи"
    )
    payment_status = models.BooleanField(default=False, verbose_name="Оплачено")

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return (
            f"{self.user} - {self.procedure}"
        )
