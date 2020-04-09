from django.urls import path,include
from django.contrib.auth import urls
from accounts.views import UserCreateView,UpdateProfileView
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('signup/',UserCreateView.as_view(),name = 'signup'),
    path('login/',LoginView.as_view(template_name='accounts/login.html'),name = 'login'),
    path('logout/',LogoutView.as_view(),name = 'logout'),
    path('profile/<slug:slug>/',UpdateProfileView.as_view(),name = 'profile')
]