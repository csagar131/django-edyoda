from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from accounts.models import User
from django.views import View
from accounts.forms import ElderSignupForm,YoungerSignupForm


# Create your views here.

class ElderUserCreate(CreateView):
    form_class = ElderSignupForm
    template_name = 'signup_elder.html'
    success_url = '/accounts/login'

    

class YoungerUserCreate(CreateView):
    form_class = YoungerSignupForm
    template_name = 'signup_younger.html'
    success_url = '/accounts/login'


class DisplayProfileView(View):
    def get(self,request,id,*args,**kwargs):
        return render(request,'profile.html')


