from django.contrib import admin
from .models import Product, Category, ProductInstance, Chat

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'name')

class ProductAdmin(admin.ModelAdmin):
    list_display=('name', 'price', 'owner')

class BookInstanceAdmin(admin.ModelAdmin):
    list_display=('product', 'status','borrower', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('product', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

class ChatAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_on')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInstance, BookInstanceAdmin)
admin.site.register(Chat, ChatAdmin)

