from django.shortcuts import render

from .selectors import get_appointments_by_client


def notes_page(request, client_id):
    appointments = get_appointments_by_client(client_id)
    context = {
        "appointments": appointments,
        "has_appointments": appointments.exists(),
    }

    return render(request, "notes.html", context=context)
