from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework import serializers

from rest_framework.views import APIView

from .models import Room
from .serializers import RoomSerializer, EventSerializer
from .services import create_room, create_event


class CreateAndListRoomAPIView(APIView):
    serializer_class = RoomSerializer

    def post(self, request, *args, **kwargs):
        serializer = RoomSerializer(data=request.data)
        created_room = create_room(serializer=serializer)

        return Response(RoomSerializer(created_room).data, status=HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        response_data = RoomSerializer(Room.objects.all(), many=True).data
        return Response(response_data, status=HTTP_200_OK)


class CreateEventAPIView(APIView):
    class CreateEventSerializer(serializers.Serializer):
        date = serializers.DateField()
        type = serializers.CharField()

        def validate_type(self, value):
            valid_types = ['private', 'public']
            if value not in valid_types:
                raise serializers.ValidationError(f'type must be one of the following values: {valid_types}')
            return value

    serializer_class = CreateEventSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.CreateEventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        created_event = create_event(room_id=self.kwargs['room_id'], **serializer.validated_data)
        return Response(EventSerializer(created_event).data, status=HTTP_200_OK)
