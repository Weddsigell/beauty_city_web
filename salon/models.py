from django.db import models


class Salon(models.Model):
    title = models.CharField("Название", max_length=200)
    address = models.CharField("Адрес", max_length=300)
    phone = models.CharField("Телефон", max_length=20)
    image = models.ImageField("Фото", upload_to="salons/", blank=True)

    class Meta:
        verbose_name = "Салон"
        verbose_name_plural = "Салоны"

    def __str__(self):
        return self.title
    