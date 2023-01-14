from django.db import models
from common.models import CommonModel

# Create your models here.


class Category(CommonModel):
    """Room or Experience Category"""

    class CategoryKindChoices(models.TextChoices):
        ROOM = ("rooms", "Rooms")
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(max_length=50)
    kind = models.CharField(
        max_length=15,
        choices=CategoryKindChoices.choices,
    )

    def __str__(self) -> str:
        return f"{self.kind.title()} : {self.name}"  # title() 첫 스펠링 대문자

    class Meta:
        verbose_name_plural = "Cateogories"
