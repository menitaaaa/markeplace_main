from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Product

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_seller')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'categories']