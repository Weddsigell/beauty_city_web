from .models import Salon


def get_salons():
    return Salon.objects.all()
