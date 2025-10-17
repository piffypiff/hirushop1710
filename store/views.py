from django.shortcuts import render, get_object_or_404  
# render — функция для отображения HTML-шаблонов
# get_object_or_404 — возвращает объект из базы или ошибку 404, если объект не найден

from .models import Product  
# Импортируем модель Product, чтобы получать данные о товарах из базы данных


# 🏠 Главная страница магазина
def index(request):
    # Получаем все товары из базы данных
    products = Product.objects.all()

    # Передаём список товаров в шаблон 'store/index.html'
    # В шаблоне мы сможем обращаться к ним через переменную 'products'
    return render(request, 'store/index.html', {'products': products})


# 🛒 Страница конкретного товара
def product_detail(request, product_id):
    # Пытаемся получить товар по его ID (product_id)
    # Если товара с таким ID нет — автоматически покажется страница 404
    product = get_object_or_404(Product, pk=product_id)

    # Отображаем шаблон 'store/product_detail.html' и передаём туда товар
    return render(request, 'store/product_detail.html', {'product': product})


# Create your views here.
# (Эта строка создаётся Django автоматически — можно оставить или удалить)
