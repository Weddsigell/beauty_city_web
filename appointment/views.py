from django.shortcuts import render

from .selectors import get_appointments_by_client


def render_notes(request):
    appointments = get_appointments_by_client(client_id=request.GET.get("client_id"))
    context = {
        "appointments": appointments,
        "has_appointments": appointments.exists(),
    }

    return render(request, "notes.html", context=context)
