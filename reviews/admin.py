from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),  # 첫번째는 url에 나타나는 값, 두번째는 admin패널에 나타나는 값
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        # print(request.GET)  # url을 읽어옴
        # print(self.value())
        # print(self.value())
        print(request.GET)
        word = self.value()  # 잘 모르겠음..;;;
        print(self)

        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews


class ConfirmReviewFilter(admin.SimpleListFilter):
    title = "ConfirmReview"
    parameter_name = "assessment"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]

    def queryset(self, request, reviews):

        assessment = self.value()
        print(self)
        print(assessment)
        if assessment == "good":
            return reviews.filter(rating__gt=3)
        elif assessment == "bad":
            return reviews.filter(rating__lt=4)
        return reviews


# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = [
        "__str__",
        "payload",
    ]
    list_filter = [
        WordFilter,
        ConfirmReviewFilter,
        "rating",
        "user__is_host",  # 왜래키가 설정된 테이블의 다른 필드 값도 __(lookup)으로 filtering가능함
        "room__category",
        "room__pet_friendly",
    ]
