from django.shortcuts import render

def index(request):
    return render(request, 'full_app/index.html')

def cart(request):
    return render(request, 'full_app/cart.html')

def category(request):
    return render(request, 'full_app/category.html')

def ckeckout(request):
    return render(request, 'full_app/checkout.html')

def contact(request):
    return render(request, 'full_app/contact.html')

def product(request):
    return render(request, 'full_app/product.html')

