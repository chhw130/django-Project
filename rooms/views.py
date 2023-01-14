from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.


def say_hello(request):  # request 요청을 보내는 유저정보들의 객체
    return HttpResponse("hello")


def see_all_rooms(request):
    data = Room.objects.all()
    return render(
        request,
        "all_rooms.html",
        {
            "datas": data,
            "title": "hello!",
        },
    )


def see_one_room(request, room_id):
    try:
        data = Room.objects.get(pk=room_id)
        return render(
            request,
            "room_detail.html",
            {
                "data": data,
            },
        )
    except Room.DoesNotExist:
        return render(
            request,
            "room_detail.html",
            {
                "not_found": True,
            },
        )
