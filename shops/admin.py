from django.contrib import admin

from .models import Category,Product,Cart,CartItem


class CategoryAdmin(admin.ModelAdmin):
    list_display =["name"]
class ProductAdmin(admin.ModelAdmin):
   list_display=["name","price","category"]
class CartAdmin(admin.ModelAdmin):
   list_display =["created_at"]
class CartItemAdmin(admin.ModelAdmin):
   list_display =["cart","product","quantity"]



admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem,CartItemAdmin)