from rest_framework import serializers

from .models import Room, Event, Book


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'capacity'
        ]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'date',
            'type',
            'room_id'
        ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'date',
            'capacity',
            'customer_id'
        ]


class CreateEventSerializer(serializers.Serializer):
    date = serializers.DateField()
    type = serializers.CharField()

    def validate_type(self, value):
        valid_types = ['private', 'public']
        if value not in valid_types:
            raise serializers.ValidationError(f'type must be one of the following values: {valid_types}')
        return value


class CreatePlaceBookSerializer(serializers.Serializer):
    requested_capacity = serializers.IntegerField()