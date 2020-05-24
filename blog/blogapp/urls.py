from django.urls import path
from blogapp import views  # импортируем вьюшки


app_name = 'blogapp'

# связываем вьюшки с адресами
urlpatterns = [
    path('', views.main_view, name='index'),
    path('create/', views.contact_view, name='create'),
    path('post/<int:id>/', views.post, name='post')
]
