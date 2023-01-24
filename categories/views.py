from django.shortcuts import render
from .models import Category
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializers


# from django.core import serializers
# Create your views here.


@api_view(["POST", "GET"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializers(
            all_categories,
            many=True,
        )  # CategorySerializers가 직렬화 할 데이터보다 많은 것을 넘겨주어 many=True를 해주어야함
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializers(
            data=request.data
        )  # request.data 사용자가 post한 데이터 // data=을 통해 serialize
        if serializer.is_valid():  # 데이터 타당성 검사
            new_category = serializer.save()
            return Response(CategorySerializers(new_category).data)
        else:
            return Response(serializer.errors)  # 데이터 에러확인

    # 쿼리셋 형태 데이터를 json화 해주어 api에 나타내주어야함.

    # {"name": "Category from DRF", "kind": "rooms"}


@api_view()
def category(request, pk):
    one_category = Category.objects.get(pk=pk)
    serializer = CategorySerializers(one_category)
    return Response(serializer.data)
