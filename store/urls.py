from django.urls import path  
from . import views            # Импортируем наши функции (представления) из файла views.py

# Здесь мы указываем, какие URL-адреса обрабатывает это приложение
urlpatterns = [
    # Главная страница магазина (например, http://127.0.0.1:8000/)
    path('', views.index, name='index'),

    # Страница конкретного товара (например, http://127.0.0.1:8000/product/5/)
    # <int:product_id> — это динамическая часть URL: Django подставит ID товара из базы
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
