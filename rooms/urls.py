from django.urls import path
from rooms import views

urlpatterns = [
    path("", views.say_hello),
    path("<int:room_id>/", views.see_one_room),
    path("all/", views.see_all_rooms),
]
