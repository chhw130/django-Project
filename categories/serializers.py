from rest_framework import serializers
from .models import Category


class CategorySerializers(serializers.Serializer):

    pk = serializers.IntegerField(
        read_only=True
    )  # read_only를 통해 pk는 입력안하고 유저가 post할수 있음
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.ChoiceField(
        choices=Category.CategoryKindChoices.choices,
    )
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

        # **을 사용하면 {"name" : "category"}를
        # name = "category"로 바꿈
