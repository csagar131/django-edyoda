from django.urls import path,include
from blog.views import PostListCreateAPIVIew,PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('posts',PostListCreateAPIVIew.as_view()),
    path('posts/<int:pk>',PostRetrieveUpdateDestroyAPIView.as_view())
]