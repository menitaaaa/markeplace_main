from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from .models import Product, Category, Cart, CartItem

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'products': products, 'categories': categories})

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')
    return render(request, 'store/register.html', {'form': form})