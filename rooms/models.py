from django.db import models
from common.models import CommonModel

# Create your models here.


class Room(CommonModel):
    """
    Room Model Definition
    """

    class RoomKindChoices(models.TextChoices):
        # 첫번째 db에 들어갈 값, admin에 선택값
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",  # 외래키_set 이름을 바꾸어줌.
    )  # 다른 모델 외래키
    amenities = models.ManyToManyField(
        "rooms.Amenity",
        related_name="rooms",
    )  # 다대다로 연결
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="rooms",
    )

    def __str__(self) -> str:
        return self.name

    # def total_amenities(self):
    #     print(self)
    #     return "hello"
    def rating(self):
        return self.reviews.count()

    def rating_average(self):
        count = self.reviews.count()
        data = self.reviews.all().values("rating")
        # data = self.reviews.all()  # 장고에서 모든 review 데이터를 보기 때문에 비효율적
        if count == 0:
            return "No Reviews"
        else:
            total_rating = 0
            for review in data:
                total_rating += review["rating"]
        return round(total_rating / len(data), 2)


class Amenity(CommonModel):
    """Amenity Definition"""

    name = models.CharField(max_length=150)
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"  # class 이름을 바꿈
