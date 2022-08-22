from django.urls import path

from . import views

urlpatterns = [
    path('room/', views.CreateAndListRoomAPIView.as_view()),
    path('room/event/', views.RetrievePublicEventsAPIView.as_view()),
    path('room/event/book/<str:book_id>/', views.GetAndDeletePlaceBookAPIView.as_view()),
    path('room/event/book/', views.GetAndDeletePlaceBookAPIView.as_view()),
    path('room/<str:room_id>/event/', views.CreateEventAPIView.as_view()),
    path('room/<room_id>/event/<event_id>/book/', views.CreatePlaceBookAPIView.as_view())
]