import master
from .models import Master, ScheduleMaster


def get_masters():
    return Master.objects.all()


def get_shedule_masters(master_id):
    base_shedule = ScheduleMaster.objects.get(master=master_id)
    notes_shedule = 1
    relative_shedule = base_shedule.schedules.all()