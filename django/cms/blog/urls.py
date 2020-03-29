from django.contrib import admin
from django.urls import path,include
from blog.views import index,blog_details,contact_view,post_model_form,post_edit_model_form
from blog.views import category_index


urlpatterns = [
    path('',index),
    path('',category_index),
    path('<int:id>',blog_details),
    path('contact',contact_view),
    path('posts',post_model_form),
    path('posts/<int:id>',post_edit_model_form),
]
