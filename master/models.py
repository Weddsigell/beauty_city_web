from django.db import models
from django.utils import timezone


class Specialization(models.Model):
    name = models.CharField(
        max_length=40,
        verbose_name="Специализация",
        unique=True,
    )

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"

    def __str__(self):
        return self.name


class Master(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    photo = models.ImageField(verbose_name="Фото", upload_to="masters_photo/")
    start_work = models.DateField(verbose_name="Начало стажа работы")
    salon = models.ForeignKey(
        "salon.Salon",
        on_delete=models.CASCADE,
        verbose_name="Салон",
        related_name="masters",
    )
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.SET_NULL,
        verbose_name="Специализация",
        related_name="masters",
        null=True,
    )

    class Meta:
        verbose_name = "Мастера"
        verbose_name_plural = "Мастера"

    @property
    def experience(self):
        delta = timezone.now().date() - self.start_work
        return delta.days // 30

    def __str__(self):
        return f"{self.name} {self.experience} месяцев"


class ScheduleMaster(models.Model):
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
    interval = models.PositiveSmallIntegerField(
        verbose_name="Интервал",
        default=120,
    )
    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        verbose_name="Мастер",
        related_name="schedules",
    )
    is_active = models.BooleanField(
        default=True, verbose_name="Активно(выходной или нет)"
    )

    class Meta:
        verbose_name = "Расписание мастера"
        verbose_name_plural = "Расписания мастеров"
        unique_together = ["master", "day"]
        ordering = ["day"]

    def __str__(self):
        return f"{self.master} c {self.start_time} до {self.end_time}"
