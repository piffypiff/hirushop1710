from django.apps import AppConfig


# Создаём класс конфигурации приложения "store"
# Этот класс сообщает Django, что это отдельное приложение (модуль)
class StoreConfig(AppConfig):
    """
    Этот класс — "паспорт" нашего приложения store.
    Он регистрирует его внутри проекта Django.
    """

    # По умолчанию Django создаёт поля с типом BigAutoField
    # (это большие автоинкрементные ID для моделей)
    default_auto_field = 'django.db.models.BigAutoField'

    # Название приложения — оно должно совпадать с папкой приложения
    name = 'store'
