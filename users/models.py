from django.contrib.auth.models import AbstractUser  # 추가
from django.db import models

# Create your models here.


class User(AbstractUser):  # AbstractUser를 상속함

    bio = models.TextField(default="")
