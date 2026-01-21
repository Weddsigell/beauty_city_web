from django.db import models


class Note(models.Model):
    client = models.ForeignKey(
        "client.Client", on_delete=models.CASCADE, verbose_name="Клиент"
    )
    master = models.ForeignKey(
        "master.Master",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Мастер",
    )
    service = models.ForeignKey(
        "service.Service",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Услуга",
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
            f"{self.client} - {self.price} - "
            f"{self.master} - {self.service} - "
            f"{self.date} - {self.time}"
        )
