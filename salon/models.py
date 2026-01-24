from django.db import models


class Salon(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    photo = models.ImageField(verbose_name="Фото", upload_to="salon_photo/")
    address = models.CharField(max_length=100, verbose_name="Адрес")

    class Meta:
        verbose_name = "Салон"
        verbose_name_plural = "Салоны"

    def __str__(self):
        return f"{self.name} {self.address}"


class ScheduleSalon(models.Model):
    day = models.PositiveSmallIntegerField(
        choices=(
            (0, "Понедельник"),
            (1, "Вторник"),
            (2, "Среда"),
            (3, "Четверг"),
            (4, "Пятница"),
            (5, "Суббота"),
            (6, "Воскресенье"),
        ),
        verbose_name="День недели",
    )
    start_time = models.TimeField(verbose_name="Начало рабочего времени")
    end_time = models.TimeField(verbose_name="Окончание рабочего времени")
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, verbose_name="Салон", related_name="schedules")
    is_active = models.BooleanField(
        default=True, verbose_name="Активно(выходной или нет)"
    )

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"
        unique_together = ["salon", "day"]
        ordering = ["day"]

    def __str__(self):
        return f"{self.salon} c {self.start_time} до {self.end_time}"
