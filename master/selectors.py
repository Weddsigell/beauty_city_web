from .models import Master, Specialization


def get_all_masters():
    return Master.objects.all()


def get_all_specialization():
    return Specialization.objects.all()
