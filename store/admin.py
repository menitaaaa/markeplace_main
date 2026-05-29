from django.contrib import admin
from .models import User, Category, Product, Cart, CartItem

# Configuración para Categorías
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Configuración para Productos
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Solo ponemos nombre, precio y stock para que no falle
    list_display = ('name', 'price', 'stock')

# Registros simples para el resto de modelos
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(CartItem)