from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from master.selectors import get_masters
from procedure.selectors import get_categories
from salon.selectors import get_salons

from .selectors import past_notes_by_client, upcoming_notes_by_client


@login_required
def render_notes(request):
    past_notes = past_notes_by_client(client_id=request.user.client.id)
    upcoming_notes = upcoming_notes_by_client(client_id=request.user.client.id)
    context = {
        "past_notes": past_notes,
        "upcoming_notes": upcoming_notes,
        "has_past_notes": past_notes.exists(),
        "has_upcoming_notes": upcoming_notes.exists(),
        "sum": sum([note.procedure.price for note in upcoming_notes]),
    }

    return render(request, "notes.html", context=context)


def render_categories(request):
    context = {
        "categories": get_categories(),
    }

    return render(request, "procedures.html", context=context)


def render_masters(request):
    context = {
        "masters": get_masters(),
    }

    return render(request, "masters.html", context=context)


def render_salons(request):
    context = {
        "salons": get_salons(),
    }

    return render(request, "salons.html", context=context)


def render_time(request):
    context = {}

    return render(request, "time.html", context=context)


def render_record_finaly(request):
    context = {}
    return render(request, "record_finaly.html", context=context)
