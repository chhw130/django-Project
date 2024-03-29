from django.db import models
from common.models import CommonModel

# Create your models here.


class Experience(CommonModel):
    """Experience Model Definition"""

    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    name = models.CharField(max_length=250)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=20)
    start = models.TimeField()  # DateTimeField는 년도 월 일 까지
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField("experiences.Perk")
    category = models.ForeignKey(
        "categories.Category", on_delete=models.SET_NULL, blank=True, null=True
    )  # 이해 필요

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):
    """What is included on an Experience"""

    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=250, blank=True, null=True)
    explanation = models.TextField(blank=True, default="")

    def __str__(self) -> str:
        return self.name
