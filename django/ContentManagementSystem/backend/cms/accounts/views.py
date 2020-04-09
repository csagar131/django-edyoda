from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from accounts.forms import SignUpForm,UpdateProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from accounts.models import Profile


class UserCreateView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = "/stories"


class UpdateProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'accounts/update_profile.html'
    success_url = 'accounts/profile'
    