from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, User

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user','created_at']
    list_filter = ['created_at']
    search_fields = ['text','user_username']