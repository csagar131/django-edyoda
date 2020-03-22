from django.contrib import admin
from django.urls import include,path
from items.views import index,products,product_details

urlpatterns = [
    path('',index),
    path('<str:category>',products),
    path('<str:category>/<str:product_details>',product_details)
]