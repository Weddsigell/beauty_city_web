from .models import Procedure


def get_procedures():
    return Procedure.objects.all()
