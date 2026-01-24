from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Procedure(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", unique=True)
    photo = models.ImageField(verbose_name="Фото", upload_to="procedure_photo/")
    price = models.PositiveSmallIntegerField(verbose_name="Цена")
    master = models.ManyToManyField(
        "master.Master",
        verbose_name="Мастер",
        related_name="procedures",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="procedures",
    )

    class Meta:
        verbose_name = "Процедура"
        verbose_name_plural = "Процедуры"

    def __str__(self):
        return f"{self.name} {self.price}"
