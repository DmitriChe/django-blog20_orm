from django.db import models


# Create your models here.
class Category(models.Model):  # декларативное создание модели, вклачается ORM - отображение объектов на БД
    # Id не надо, он уже сам появиться, а остальные поля модели прописываем: поле name и description
    name = models.CharField(max_length=16, unique=True)
    description = models.TextField(blank=True)

    # Основные типы полей
    # дата
    # models.DateField
    # models.DateTimeField
    # models.TimeField
    # # Числа
    # models.IntegerField
    # models.PositiveIntegerField
    # models.PositiveSmallIntegerField
    # models.FloatField
    # models.DecimalField
    # # Логический
    # models.BooleanField
    # # Байты (blob)
    # models.BinaryField
    # # Картинка
    # models.ImageField
    # # Файл
    # models.FileField
    # # url, email
    # models.URLField
    # models.EmailField

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=32, unique=True)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # Связь с категорией
    # один - много
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Связь с тегом: много - много
    tags = models.ManyToManyField(Tag)
    # Картинка
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    # для красивого отображения названия модели в админке:
    def __str__(self):
        return self.name
