from django.db import models


class Appointment(models.Model):
    client = models.ForeignKey("client.Client", on_delete=models.CASCADE)
    master = models.ForeignKey(
        "master.Master", on_delete=models.SET_NULL, null=True, blank=True
    )
    service = models.ForeignKey(
        "service.Service", on_delete=models.SET_NULL, null=True, blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return (
            f"{self.client} - {self.price} - "
            f"{self.master} - {self.service} - "
            f"{self.date} - {self.time}"
        )
