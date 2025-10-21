from django.db import models

# 👤 Пользователь (своя простая версия модели User)
class User(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(unique=True, verbose_name="Email")
    bio = models.TextField(blank=True, verbose_name="Описание / Биография")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # 💪 Дополнительный метод — вывод полного имени
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


# 📰 Статья, связанная с пользователем
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles", verbose_name="Автор")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

from django.db import models

# Комментарии к статьям
class Comment(models.Model):
    article = models.ForeignKey(
        'accounts.Article',  # ссылаемся на Article из accounts
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Статья"
    )
    author_name = models.CharField(max_length=100, verbose_name="Автор комментария")
    text = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Комментарий от {self.author_name} к '{self.article.title}'"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"



# Create your models here.
