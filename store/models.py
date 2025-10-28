from django.db import models



# МОДЕЛЬ КАТЕГОРИИ
class Category(models.Model):
    # Название категории (например: "Мышки", "Клавиатуры", "Коврики")
    name = models.CharField(max_length=100, unique=True, verbose_name="Название категории")

    # Чтобы в админке отображалось понятное имя категории
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"              # Название модели в единственном числе
        verbose_name_plural = "Категории"       # Название модели во множественном числе


# МОДЕЛЬ ТОВАРА
class Product(models.Model):
    # Название товара (например: "Logitech GPX Superlight")
    name = models.CharField(max_length=100, verbose_name="Название товара")

    # Описание товара
    description = models.TextField(blank=True, verbose_name="Описание")

    # Цена (максимум 10 цифр, из них 2 после запятой)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    # Картинка товара (сохраняется в папку media/products/)
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Изображение")

    # Категория, к которой принадлежит товар (ForeignKey = связь многие-к-одному)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,      # если удалить категорию — удалятся и товары в ней
        related_name='products',       # доступ к товарам через category.products.all()
        verbose_name="Категория"
    )

    # Возвращает название товара при отображении в админке
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"         # Название модели в единственном числе
        verbose_name_plural = "Товары" # Название модели во множественном числе
