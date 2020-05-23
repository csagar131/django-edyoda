from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView,UpdateView
from accounts.models import User
from django.views import View
from accounts.forms import ElderSignupForm,YoungerSignupForm,EditProfileForm


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
    def get(self,request,slug,*args,**kwargs):
        return render(request,'profile.html')


class EditProfileView(UpdateView):
    model = User
    template_name = 'editprofile.html'
    form_class = EditProfileForm
    success_url = 'profile'

    def get_success_url(self,*args,**kwargs):
        # if 'slug' in self.kwargs:
        #     slug = self.kwargs['slug']
        # else:
        #     slug = 'demo'
        return reverse('profile', kwargs={'slug': self.object.slug})



