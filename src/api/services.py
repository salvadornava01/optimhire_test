from .models import Room, Event
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
    room_found = Room.objects.get(id=room_id)
    events_found = Event.objects.filter(room=room_id, date=date)
    # Check if an event already exists
    if len(events_found):
        raise Exception('Event already exists')
    created_event = Event.objects.create(date=date, type=type, room=room_found)
    return created_event
