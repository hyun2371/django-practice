from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # profile = models.OneToOneField() 역참조 필드 생성됨
    # user.order_set.all() 일대다 조회
    pass


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
