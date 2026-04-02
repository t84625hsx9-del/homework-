from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name=models.CharField(max_length=15)
    email=models.EmailField(verbose_name="Электронная почта", unique=True)
    bio=models.TextField(max_length=300, blank=True)
    birth_date=models.DateField(null=True, blank=True)
    favourite_pet=models.CharField(max_length=50, blank=True)
