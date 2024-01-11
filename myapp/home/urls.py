from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path("about",views.about,name='aboutus'),
    path("servers", views.servers, name='servers'),
    path("contact", views.contact, name='contact'),

]
