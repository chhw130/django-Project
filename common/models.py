from django.db import models

# Create your models here.
class CommonModel(models.Model):  # 모델들이 공통으로 가져야하는 값을 상속하는 app
    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # 실제 데이터로 사용되지 않음
