from django.contrib import admin
from .models import User, Article

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "created_at")

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    
from .models import Comment

admin.site.register(Comment)



# Register your models here.
