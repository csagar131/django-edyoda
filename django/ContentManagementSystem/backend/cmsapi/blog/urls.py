from django.urls import path,include
from blog.views import PostAPIView

urlpatterns = [
    path('posts',PostAPIView.as_view()),
]