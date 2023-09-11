from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='телефон', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True, null=True)
    country = models.CharField(max_length=15, verbose_name='страна', blank=True, null=True)
    is_verified = models.BooleanField(verbose_name='подтверждён', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
