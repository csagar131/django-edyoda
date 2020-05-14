from django.urls import path,include
from userprofile.views import UserCreateFormView
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('singup',UserCreateFormView.as_view(),name = 'signup'),
    path('login',LoginView.as_view(template_name='login.html'),name = 'login'),
    path('logout',LogoutView.as_view(),name = 'logout'),
]