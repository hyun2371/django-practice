from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class CustomUserManager(models.Manager):
    def with_image(self): # 자주 사용되는 쿼리 패턴을 함수로 정의
        return super().get_queryset().filter(image__isnull=False) #이미지가 존재하는 사용자만 조회

class CustomUser(AbstractUser):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True
    )
    # media/profiles/.jpg
    image = models.ImageField(
        upload_to="profiles/",
        null=True,
    )
    preferences = models.JSONField(default=dict)

    objects = CustomUserManager()