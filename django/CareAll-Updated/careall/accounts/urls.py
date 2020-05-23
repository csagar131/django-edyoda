from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from accounts.views import ElderUserCreate,YoungerUserCreate,DisplayProfileView,EditProfileView


urlpatterns = [
    path('signup/elder',ElderUserCreate.as_view(),name = 'signup_elder'),
    path('signup/younger',YoungerUserCreate.as_view(),name = 'signup_younger'),
    path('login',LoginView.as_view(template_name='login.html'),name = 'login'),
    path('logout',LogoutView.as_view(),name = 'logout'),
    path('profile/<slug:slug>',DisplayProfileView.as_view(),name = 'profile'),
    path('profile/update/<slug:slug>',EditProfileView.as_view(),name = 'editprofile'),
]