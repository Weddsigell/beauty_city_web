import time
from .models import Note
from django.utils import timezone


def upcoming_notes_by_client(id):
    date_now = timezone.now().date()
    time_now = timezone.now().time()
    try:
        return Note.objects.filter(id=id, date__gte=date_now, time__gte=time_now)
    except (AttributeError, ValueError) as e:
        raise e


def past_notes_by_client(id):
    date_now = timezone.now().date()
    time_now = timezone.now().time()
    try:
        return Note.objects.filter(id=id, date__lt=date_now, time__lt=time_now)
    except (AttributeError, ValueError) as e:
        raise e
