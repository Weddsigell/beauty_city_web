from .models import Appointment


def create_appointment(client, master, service, date, time, price):
    Appointment.objects.create(
        client=client, master=master, service=service, date=date, time=time, price=price
    )
