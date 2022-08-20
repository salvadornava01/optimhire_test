from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from rest_framework.views import APIView

from .models import Room
from .serializers import RoomSerializer
from .services import create_room


class CreateAndListRoomAPIView(APIView):

    serializer_class = RoomSerializer

    def post(self, request, *args, **kwargs):
        serializer = RoomSerializer(data=request.data)
        created_room = create_room(serializer=serializer)

        return Response(RoomSerializer(created_room).data, status=HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        response_data = RoomSerializer(Room.objects.all(), many=True).data
        return Response(response_data, status=HTTP_200_OK)
