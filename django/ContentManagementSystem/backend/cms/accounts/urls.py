from django.urls import path,include
from django.contrib.auth import urls
from accounts.views import UserCreateView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('',include(urls)),
    path('signup/',UserCreateView.as_view()),
    path('login/',LoginView.as_view(template_name='accounts/login.html'),name = 'login'),
]