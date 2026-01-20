from django.db import models
from salon.models import Salon 
from service.models import Service

class Master(models.Model):
    CHOICE_SPECIALIZATION = [
        ('stylist', 'стилист'),
        ('make-up', 'визажист'),
        ('nail-master', 'мастер маникюра'),
        ('barber', 'парикмахер'),
    ]

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    speciality = models.CharField(
        choices=CHOICE_SPECIALIZATION,
        max_length=20,
        verbose_name='Специальность',
    )
    image = models.ImageField("Фото мастера", upload_to="masters_photo/", blank=True, null=True)
    salon = models.ForeignKey(
        Salon,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='masters',
        verbose_name='Салон',
    )
    services = models.ManyToManyField(
        Service,
        related_name='masters',
        verbose_name='Услуги'
    )

    class Meta:
        verbose_name = 'Мастера'
        verbose_name_plural = 'Мастера'

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.get_speciality_display()})'

