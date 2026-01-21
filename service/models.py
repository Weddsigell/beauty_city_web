from django.db import models
from django.core.validators import MinValueValidator
from salon.models import Salon

class Service(models.Model):
    SERVICES = [
        ('hair_services', 'Парикмахерские услуги'),
        ('nail_service', 'Ногтевой сервис'),
        ('makeup', 'Макияж')
    ]
    
    group_services = models.CharField(
        choices=SERVICES,
        max_length=100,
        verbose_name='Группа услуг',
    )
    name = models.CharField(max_length=100, verbose_name='Услуга')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(1)],
        verbose_name='Цена',
    )
    salons = models.ManyToManyField(
        Salon,
        related_name='services',
        verbose_name='Доступно в салонах'
    )

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return f'{self.name}'