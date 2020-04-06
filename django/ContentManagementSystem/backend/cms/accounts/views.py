from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin


class UserCreateView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = "/stories"