from django.contrib import admin
from .models import Room, Amenity

# Register your models here.


@admin.action(description="Set all prices to zero")
def reset_prices(
    model_admin, request, rooms
):  # first_parameter : 이 액션을 호출하는 클래스 / second_parameter : 이 액션을 요청하는 user의 요청 정보 / third_parameter : 선택된 방에 대한 qeryset
    # print(rooms == rooms.all())
    # print(request)
    print(rooms)

    # print(rooms)
    # print(rooms.all())
    for room in rooms:
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)

    list_display = [
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "rating_average",
        "owner",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "^name",  # ^를 사용하여 ~시작하는 것 검색
        "=price",  # 검색한 값과 반드시 같은 값만 검색
        "owner__username",  # username?? 그냥 name은..?
    ]

    list_filter = [
        "country",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    ]

    def total_amenities(self, room):
        return room.amenities.count()


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = ["name", "description", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
