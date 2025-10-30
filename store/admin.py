from django.contrib import admin
from .models import Product, Category, ProductSpecification

# Встроенная таблица для добавления характеристик прямо внутри карточки товара
class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    extra = 1  # Показывает одну пустую строку для добавления новой характеристики

# Админка для товаров с характеристиками
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    inlines = [ProductSpecificationInline]

# Категории регистрируются отдельно
admin.site.register(Category)


# Register your models here.
