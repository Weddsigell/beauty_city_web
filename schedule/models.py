from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


class Schedule(models.Model):
    master = models.ForeignKey(
        'master.Master',
        on_delete=models.CASCADE,
        verbose_name="Мастер"
    )
    salon = models.ForeignKey(
        'salon.Salon',
        on_delete=models.CASCADE,
        verbose_name="Салон"
    )
    date = models.DateField(verbose_name="Дата")
    start_time = models.TimeField(verbose_name="Начало рабочего времени")
    end_time = models.TimeField(verbose_name="Окончание рабочего времени")
    services = models.ManyToManyField(
        'service.Service',
        verbose_name="Доступные услуги",
        blank=True
    )

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"
        unique_together = ('master', 'salon', 'date')
        ordering = ['date', 'start_time']

    def __str__(self):
        return f"{self.master} - {self.salon} - {self.date} ({self.start_time}-{self.end_time})"
