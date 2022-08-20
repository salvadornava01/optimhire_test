from rest_framework.views import APIView

from .models import Room
from .selectors import get_public_events, get_all_booked_places
from .serializers import RoomSerializer, EventSerializer, BookSerializer, CreateEventSerializer, \
    CreatePlaceBookSerializer
from .services import create_room, create_event, book_place, cancel_book
from utils.query_param_utils import get_query_param_or_bad_request
from utils.api_responses import SuccessAPIResponse

from optimhiretest.custom_exception_middleware import CustomViewException


class CreateAndListRoomAPIView(APIView):
    serializer_class = RoomSerializer

    def post(self, request, *args, **kwargs):
        serializer = RoomSerializer(data=request.data)
        created_room = create_room(serializer=serializer)

        return SuccessAPIResponse(RoomSerializer(created_room).data)

    def get(self, request, *args, **kwargs):
        response_data = RoomSerializer(Room.objects.all(), many=True).data
        return SuccessAPIResponse(response_data)


class CreateEventAPIView(APIView):
    serializer_class = CreateEventSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreateEventSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomViewException(serializer.errors, 400)
        created_event = create_event(room_id=self.kwargs['room_id'], **serializer.validated_data)
        return SuccessAPIResponse(EventSerializer(created_event).data)


class CreatePlaceBookAPIView(APIView):
    serializer_class = CreatePlaceBookSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreatePlaceBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer_id = get_query_param_or_bad_request('customer_id', request.query_params)
        event_id = self.kwargs['event_id']
        room_id = self.kwargs['room_id']
        booked_place = book_place(room_id=room_id, event_id=event_id, **serializer.validated_data,
                                  customer_id=customer_id)
        return SuccessAPIResponse(BookSerializer(booked_place).data)


class GetAndDeletePlaceBookAPIView(APIView):

    def get(self, request, *args, **kwargs):
        all_booked_places = get_all_booked_places()
        return SuccessAPIResponse(BookSerializer(all_booked_places, many=True).data)

    def delete(self, request, *args, **kwargs):
        customer_id = get_query_param_or_bad_request('customer_id', request.query_params)
        book_id = self.kwargs['book_id']
        cancel_book(book_id=book_id, customer_id=customer_id)
        return SuccessAPIResponse({})


class RetrievePublicEventsAPIView(APIView):

    def get(self, request, *args, **kwargs):
        public_events = get_public_events()
        return SuccessAPIResponse(EventSerializer(public_events, many=True).data)
