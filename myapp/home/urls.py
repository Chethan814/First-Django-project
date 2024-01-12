from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('https://chethan814.github.io/First-Django-project/',views.index,name='home'),
    path("https://chethan814.github.io/First-Django-project/about",views.about,name='about'),
    path("https://chethan814.github.io/First-Django-project/services", views.services, name='services'),
    path("https://chethan814.github.io/First-Django-project/contact", views.contact, name='contact'),
    path("https://chethan814.github.io/First-Django-project/product", views.product, name='product'),


]
