from django.contrib.auth.models import AbstractUser  # 추가
from django.db import models

# Create your models here.


class User(AbstractUser):  # AbstractUser를 상속함

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "english"), (LANGUAGE_KOREAN, "korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "usd"), (CURRENCY_KRW, "krw"))

    # 빈칸 허용 -> null=True는 데이터베이스에서 먹히는거고, form에서도 먹히려면 blank=True 사용
    avatar = models.ImageField(
        upload_to="avatars", blank=True
    )  # imagefiled 사용하려면 pillow 설치해야함(pipenv install Pillow)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, blank=True
    )  # 최대글자 설정, 비어있어도 괜찮음
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
