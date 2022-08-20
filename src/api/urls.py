from django.urls import path

from . import views

urlpatterns = [
    path('room/', views.CreateAndListRoomAPIView.as_view())
]