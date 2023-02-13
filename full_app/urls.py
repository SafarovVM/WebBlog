from django.urls import path, include
from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index', views.index, name = 'index'),
    path('cart', views.cart, name = 'cart'),
    path('category', views.category, name ='category'),
    path('checkout', views.ckeckout, name ='checkout'),
    path('contact', views.contact, name = 'contact'),
    path('product', views.product, name = 'product'),
]
