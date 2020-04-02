from django.contrib import admin
from django.urls import path,include
from blog.views import IndexView,CategoryIndexView,BlogDetailView,ContactFormView,PostModelFormView,PostFormUpdateView


urlpatterns = [
    path('',IndexView.as_view()),
    path('contact',ContactFormView.as_view()),
    path('posts',PostModelFormView.as_view()),
    path('posts/<slug:slug>',PostFormUpdateView.as_view()),
    path('<slug:slug>',BlogDetailView.as_view(), name = 'post-detail'),
]
