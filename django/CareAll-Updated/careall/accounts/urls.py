from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from accounts.views import ElderUserCreate,YoungerUserCreate,DisplayProfileView


urlpatterns = [
    path('signup/elder',ElderUserCreate.as_view(),name = 'signup_elder'),
    path('signup/younger',YoungerUserCreate.as_view(),name = 'signup_younger'),
    path('login',LoginView.as_view(template_name='login.html'),name = 'login'),
    path('logout',LogoutView.as_view(),name = 'logout'),
    path('profile/<int:id>',DisplayProfileView.as_view(),name = 'profile'),
]