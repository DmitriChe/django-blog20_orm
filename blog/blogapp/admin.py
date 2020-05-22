# место подключения моделей к админке (чтобы модели были видны в админке)
from django.contrib import admin
# Импортируем модели
from .models import Category, Post, Tag

# Делаем прописку
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
