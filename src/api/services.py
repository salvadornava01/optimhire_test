from rest_framework.generics import get_object_or_404

from .models import Room, Event, Book
from .serializers import RoomSerializer


def create_room(
        *,
        serializer: RoomSerializer
) -> Room:
    serializer.is_valid(raise_exception=True)
    return Room.objects.create(**serializer.validated_data)


def create_event(
        *,
        room_id,
        date,
        type
) -> Event:
    room_found = get_object_or_404(Room, id=room_id)
    events_found = Event.objects.filter(room=room_id, date=date)
    # Check if an event already exists
    if len(events_found):
        raise Exception('Event already exists')
    created_event = Event.objects.create(date=date, type=type, room=room_found)
    return created_event

def book_place(
        *,
        room_id,
        event_id,
        requested_capacity,
        customer_id
) -> Book:
    room_found = get_object_or_404(Room, id=room_id)
    event_found = get_object_or_404(Event, id=event_id)
    booked_places_by_customer = Book.objects.filter(event=event_id, customer_id=customer_id)
    if len(booked_places_by_customer):
        raise Exception(f'Customer with id {customer_id} has already booked a place for this event')
    booked_places = Book.objects.filter(event=event_id)
    filled_capacity = sum(list(map(lambda booked: booked.capacity, booked_places)))
    free_capacity = room_found.capacity - filled_capacity
    if free_capacity < requested_capacity:
        raise Exception(f'Event is full of capacity. Requested capacity: {requested_capacity}, free capacity: {free_capacity}')

    booked_place = Book.objects.create(event=event_found, date=event_found.date, capacity=requested_capacity, customer_id=customer_id)
    return booked_place
