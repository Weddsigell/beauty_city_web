from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .selectors import past_notes_by_client, upcoming_notes_by_client

@login_required
def render_notes(request):
    past_notes = past_notes_by_client(
        client_id=request.user.client.id
    )
    upcoming_notes = upcoming_notes_by_client(
        client_id=request.user.client.id
    )
    context = {
        "past_notes": past_notes,
        "upcoming_notes": upcoming_notes,
        "client": request.user.client,
        "has_past_notes": past_notes.exists(),
        "has_upcoming_notes": upcoming_notes.exists(),
    }

    return render(request, "notes.html", context=context)


@login_required
def render_services(request):
    context = {
        "salons": 1,
        "upcoming_notes": 1,
        "client": 1,
        "has_past_notes": 1,
        "has_upcoming_notes": 1,
    }

    return render(request, "service.html", context=context)
