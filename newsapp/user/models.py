from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICE =(
        (0,'USER'),
        (1,'AUTHOR'),
        (2,'ADMIN')
    )
    email = models.EmailField(unique=True)
    role = models.IntegerField(choices=ROLE_CHOICE, default=0)


