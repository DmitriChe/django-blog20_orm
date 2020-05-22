from django.core.management.base import BaseCommand
from blogapp.models import Category, Post, Tag


# from blogapp.models import Poll

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Выбираем ВСЕ категории и получает таким образом объект типа QuerySet типа списка и с доп. методами запросов
        categories = Category.objects.all()
        print(categories)
        print(type(categories))
        for item in categories:
            print(item)
            print(item.name)
            print(type(item))

        print('End')

        # Выбрать ОДНУ категорию .get
        category = Category.objects.get(name='Игрушки')
        print(category)
        print(type(category))

        # Несколько .filter
        category = Category.objects.filter(name='Игрушки')
        print(category)
        print(type(category))

        # Первый пост .first
        post = Post.objects.first()

        print(post)

        # Связанные поля - получение значений связанных полей
        # ForeignKey
        print(post.category)
        print(type(post.category))
        print(post.category.name)
        # ManyToMany
        print(post.tags.all())
        print(post.tags.first())
        print(post.tags.first().name)
        print(type(post.tags.first()))
        print(post.tags.filter(name='Один'))

        # print(Tag.objects.first().posts.all())
        # Создание новой категории
        Category.objects.create(name='Новая', description='Что то')

        # Изменение названия категории
        category = Category.objects.get(name='Новая')
        category.name = 'Измененная'
        category.save()

        # Удаление категории
        # Можно одну,
        category.delete()
        # можно несколько и даже все...
        # Category.objects.all().delete()
