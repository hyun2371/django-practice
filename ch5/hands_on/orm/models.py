from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class CustomUser(AbstractUser):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True
    )
    # media/profiles/.jpg
    image = models.ImageField(
        upload_to="profiles/",
        null=True,
    )

