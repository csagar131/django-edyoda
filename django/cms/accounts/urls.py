from django.urls import path,include
from django.contrib.auth import urls
from accounts.views import UserCreateView


urlpatterns = [
    path('',include(urls)),
    path('signup',UserCreateView.as_view()),
]