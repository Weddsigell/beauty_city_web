from .models import Note


def upcoming_notes_by_client(client_id):
    try:
        return Note.objects.filter(client=client_id)
    except (AttributeError, ValueError) as e:
        raise e


def past_notes_by_client(client_id):
    try:
        return Note.objects.filter(client=client_id)
    except (AttributeError, ValueError) as e:
        raise e
