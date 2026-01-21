from operator import ge
from django.shortcuts import render

from .selectors import past_appointments_by_client, upcoming_appointments_by_client
from beauty_city_web.client.selectors import get_client


def render_notes(request):
    past_appointments = past_appointments_by_client(
        client_id=request.GET.get("client_id")
    )
    upcoming_appointments = upcoming_appointments_by_client(
        client_id=request.GET.get("client_id")
    )
    client = get_client(request.GET.get("client_id"))
    context = {
        "past_appointments": past_appointments,
        "upcoming_appointments": upcoming_appointments,
        # "client": client,
        "has_past_appointments": past_appointments.exists(),
        "has_upcoming_appointments": upcoming_appointments.exists(),
    }

    return render(request, "notes.html", context=context)
