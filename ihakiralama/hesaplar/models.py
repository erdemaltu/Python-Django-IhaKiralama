from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):#kullancı modelini özelleştirme modeli
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
