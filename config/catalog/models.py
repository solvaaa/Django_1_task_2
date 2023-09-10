from django.db import models


# Create your models here.
def get_slug(title):
    slug = "-".join(title.split())
    return slug


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    preview = models.ImageField(verbose_name='Изображение', blank=True, null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(verbose_name='Создано', auto_now_add=True)
    modified_at = models.DateField(verbose_name='Изменено', auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.category} {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, primary_key=True)
    content = models.TextField(verbose_name='Содержимое', blank=True, null=True)
    preview = models.ImageField(verbose_name='Изображение', blank=True, null=True)
    created_at = models.DateField(verbose_name='Создано', auto_now_add=True)
    is_published = models.BooleanField(verbose_name='Опубликовано?', default=False)
    number_of_views = models.IntegerField(verbose_name='Просмотры', default=0)

    def __str__(self):
        return f"{self.title}, {self.is_published}"

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Version(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    version_number = models.FloatField(verbose_name="Номер версии")
    version_name = models.CharField(max_length=150, verbose_name="Название версии", blank=True, null=True)
    version_features = models.TextField(verbose_name="Признаки версии", blank=True, null=True)

    def __str__(self):
        return f"{self.version_number}: {self.version_name}"

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
