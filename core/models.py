from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)  # 모델이 생성된 날짜를 자동저장
    updated = models.DateTimeField(auto_now=True)  # 모델을 저장할때마다 새로운날짜로 업데이트

    class Meta:
        abstract = True  # 데이터베이스에 모델이 나타나지 않게 해줌. abstract 모델. 갖다쓰는 용도로만 쓰겠다는 느낌
