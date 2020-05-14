from django.shortcuts import render
from userprofile.forms import SignUpForm
from django.views.generic import ListView,CreateView
# Create your views here.


class UserListView(ListView):
    pass


class UserCreateFormView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = 'login.html'


