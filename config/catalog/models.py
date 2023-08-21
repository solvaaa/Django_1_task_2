from django.db import models

# Create your models here.


class Product(models.Model):
    pass

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Category(models.Model):
    pass

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
