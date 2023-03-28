from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    location = models.CharField(max_length=100,null=True)
    class Meta:
        db_table = "user"


