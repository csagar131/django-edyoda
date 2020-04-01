from django.contrib import admin
from django.urls import path,include
from blog.views import contact_view,post_model_form,post_edit_model_form
from blog.views import IndexView,CategoryIndexView,BlogDetailView


urlpatterns = [
    path('',IndexView.as_view()),
    path('<int:pk>',BlogDetailView.as_view()),
    path('contact',contact_view),
    path('posts',post_model_form),
    path('posts/<int:id>',post_edit_model_form),
]
