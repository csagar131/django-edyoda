from django.contrib import admin
from django.urls import path,include
from blog.views import post_model_form,post_edit_model_form
from blog.views import IndexView,CategoryIndexView,BlogDetailView,ContactFormView


urlpatterns = [
    path('',IndexView.as_view()),
    path('contact',ContactFormView.as_view()),
    path('posts',post_model_form),
    path('posts/<int:id>',post_edit_model_form),
    path('<slug:slug>',BlogDetailView.as_view()),
]
