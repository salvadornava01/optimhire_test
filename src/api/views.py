from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from rest_framework.views import APIView


class CreateAndListRoomAPIView(APIView):
    class CreateRoomSerializer(serializers.Serializer):
        capacity = serializers.IntegerField()

    serializer_class = CreateRoomSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.CreateRoomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(status=HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        return Response({}, status=HTTP_200_OK)
