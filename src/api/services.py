from rest_framework.generics import get_object_or_404
from rest_framework.status import HTTP_409_CONFLICT, HTTP_404_NOT_FOUND

from .models import Room, Event, Book
from .serializers import RoomSerializer
from optimhiretest.custom_exception_middleware import CustomViewException


def create_room(
        *,
        serializer: RoomSerializer
) -> Room:
    """
    Create a Room
    :param serializer:  is RoomSerializer
    :return: created Room Object
    """
    serializer.is_valid(raise_exception=True)
    return Room.objects.create(**serializer.validated_data)


def create_event(
        *,
        room_id,
        date,
        type
) -> Event:
    """
    Create an Event
    :param room_id: Is Room ID where Event is going to be created
    :param date: Is the date of the event
    :param type: Is the type of the event, must be in ['public', 'private'] values
    :return: a created Event
    """
    try:
        room_found = get_object_or_404(Room, id=room_id)
    except:
        raise CustomViewException('Room not found', HTTP_404_NOT_FOUND)
    events_found = Event.objects.filter(room=room_id, date=date)
    # Check if an event already exists
    if len(events_found):
        raise CustomViewException('Event already exists', HTTP_409_CONFLICT)
    created_event = Event.objects.create(date=date, type=type, room=room_found)
    return created_event

def book_place(
        *,
        room_id,
        event_id,
        requested_capacity,
        customer_id
) -> Book:
    """
    Books a Place
    :param room_id: Is Room ID where Book is going to be created
    :param event_id: Is Event ID where Book is going to be created
    :param requested_capacity: Is the capacity requested for Book
    :param customer_id: Is the ID of the customer
    :return: a created Book
    """
    try:
        room_found = get_object_or_404(Room, id=room_id)
    except:
        raise CustomViewException('Room not found', HTTP_404_NOT_FOUND)
    try:
        event_found = get_object_or_404(Event, id=event_id)
    except:
        raise CustomViewException('Event not found', HTTP_404_NOT_FOUND)
    booked_places_by_customer = Book.objects.filter(event=event_id, customer_id=customer_id)
    if len(booked_places_by_customer):
        raise CustomViewException(f'Customer with id {customer_id} has already booked a place for this event', HTTP_409_CONFLICT)
    booked_places = Book.objects.filter(event=event_id)

    # To calculate used_capacity, we iterate over all booked_places, get each capacity and finally sum them all
    used_capacity = sum(list(map(lambda booked: booked.capacity, booked_places)))
    free_capacity = room_found.capacity - used_capacity

    # If requested_capacity is greater than free capacity, no more capacity available
    if free_capacity < requested_capacity:
        raise CustomViewException(f'Event is full of capacity. Requested capacity: {requested_capacity}, free capacity: {free_capacity}', HTTP_409_CONFLICT)

    booked_place = Book.objects.create(event=event_found, date=event_found.date, capacity=requested_capacity, customer_id=customer_id)
    return booked_place


def cancel_book(
        *,
        book_id,
        customer_id
):
    """
    Cancel a Booked Place
    :param book_id: ID of Booked Place to be canceled
    :param customer_id: ID of the customer that request cancellation
    :return: None
    """
    try:
        booked_place_found = get_object_or_404(Book, id=book_id)
    except:
        raise CustomViewException('Not found', HTTP_404_NOT_FOUND)
    if booked_place_found.customer_id != customer_id:
        raise CustomViewException(f'Cannot cancel Booked place with ID: {book_id}, because it does not belong to customer with ID: {customer_id}', HTTP_409_CONFLICT)
    booked_place_found.delete()
    return
