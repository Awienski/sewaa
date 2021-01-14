from django.contrib import admin
from .models import Blog, Category, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'last_modified', 'author')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
