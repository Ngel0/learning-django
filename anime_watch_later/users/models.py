from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
