from .models import Room
from .serializers import RoomSerializer


def create_room(
        *,
        serializer: RoomSerializer
) -> Room:
    serializer.is_valid(raise_exception=True)
    return Room.objects.create(**serializer.validated_data)

