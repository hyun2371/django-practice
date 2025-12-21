from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # profile = models.OneToOneField() 역참조 필드 생성됨
    pass

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

# user1 -> profile1(on_delete=CASCADE) 유저1 삭제 시 프로필1도 삭제됨
