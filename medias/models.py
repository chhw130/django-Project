from django.db import models
from common.models import CommonModel

# Create your models here.


class Photo(CommonModel):

    file = models.ImageField()
    description = models.CharField(max_length=140)
    room = models.ForeignKey(
        "rooms.Room", null=True, blank=True, on_delete=models.CASCADE
    )
    experience = models.ForeignKey(
        "experiences.Experience", null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"Photo File"


class Video(CommonModel):
    file = models.FileField()
    experience = models.OneToOneField(
        "experiences.Experience", on_delete=models.CASCADE
    )  # 결제 정보 one to one 하나당 하나만 가짐

    def __str__(self) -> str:
        return f"Video File"
