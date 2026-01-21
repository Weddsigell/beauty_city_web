from .models import Appointment


def get_appointments_by_client(client_id):
    try:
        return Appointment.objects.filter(client=client_id)
    except (AttributeError, ValueError) as e:
        raise e
    
