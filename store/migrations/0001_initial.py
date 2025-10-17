# Этот файл создан автоматически при выполнении команды:
# python manage.py makemigrations
# Он содержит инструкции для создания таблиц в базе данных.

# Импортируем нужные модули Django для работы с моделями и миграциями
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Этот класс описывает миграцию — то есть шаг изменений в базе данных.
    Django будет использовать его, чтобы создать таблицы для моделей.
    """

    # Это значит, что это первая миграция (создание базы "с нуля")
    initial = True

    # Здесь могли бы быть зависимости от других приложений,
    # но в данном случае их нет (список пустой)
    dependencies = [
    ]

    # operations — список действий, которые нужно выполнить в базе данных
    operations = [

        # Создание таблицы Category (Категории товаров)
        migrations.CreateModel(
            name='Category',  # Имя модели (и таблицы)
            fields=[          # Список полей таблицы
                # Поле id — это первичный ключ, который Django создаёт автоматически
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                # Поле name — название категории, например: "Мыши", "Клавиатуры", "Коврики"
                ('name', models.CharField(
                    max_length=100,            # Максимум 100 символов
                    unique=True,               # Название категории не может повторяться
                    verbose_name='Название категории'  # Название для отображения в админке
                )),
            ],
            options={
                'verbose_name': 'Категория',          # Название в единственном числе для админки
                'verbose_name_plural': 'Категории',   # Во множественном числе
            },
        ),

        # Создание таблицы Product (Товары)
        migrations.CreateModel(
            name='Product',  # Имя модели (и таблицы)
            fields=[         # Поля таблицы
                # id — уникальный идентификатор товара
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                # name — название товара, например: "WLmouse Beast X Max"
                ('name', models.CharField(
                    max_length=100,
                    verbose_name='Название товара'
                )),

                # description — описание товара, может быть пустым (blank=True)
                ('description', models.TextField(
                    blank=True,
                    verbose_name='Описание'
                )),

                # price — цена, хранится как число с двумя знаками после запятой
                ('price', models.DecimalField(
                    max_digits=10,     # Максимум 10 цифр
                    decimal_places=2,  # Два знака после запятой
                    verbose_name='Цена'
                )),

                # image — изображение товара, сохраняется в папке "products/"
                ('image', models.ImageField(
                    upload_to='products/',  # Путь, куда сохраняются изображения
                    blank=True,             # Можно не указывать
                    null=True,              # Может быть пустым в базе
                    verbose_name='Изображение'
                )),

                # category — связь товара с категорией (ForeignKey)
                ('category', models.ForeignKey(
                    to='store.category',                    # Связь с таблицей Category
                    on_delete=django.db.models.deletion.CASCADE,  # Если категорию удалить, все её товары тоже удаляются
                    related_name='products',                # Обратная ссылка: category.products
                    verbose_name='Категория'
                )),
            ],
            options={
                'verbose_name': 'Товар',          # Название в единственном числе для админки
                'verbose_name_plural': 'Товары',  # Во множественном числе
            },
        ),
    ]
