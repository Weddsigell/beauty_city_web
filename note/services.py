from .models import Note


def create_note(client, master, service, date, time, price):
    Note.objects.create(
        client=client, master=master, service=service, date=date, time=time, price=price
    )


def fname(arg):
    pass
