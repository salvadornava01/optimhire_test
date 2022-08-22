from typing import Iterable

from .models import Event, Book


def get_public_events() -> Iterable[Event]:
    public_events = Event.objects.filter(type='public')
    return public_events


def get_all_booked_places() -> Iterable[Book]:
    booked_places = Book.objects.all()
    return booked_places
