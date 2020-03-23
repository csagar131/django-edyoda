from django.contrib import admin
from django.urls import path,include
from blog.views import index,blog_details,contact_view


urlpatterns = [
    path('',index),
    path('<int:id>',blog_details),
    path('contact',contact_view),
]
