from django.contrib import admin
from django.urls import include,path
from items.views import index,products

urlpatterns = [
    path('',index),
    path('<str:category>',products),
]