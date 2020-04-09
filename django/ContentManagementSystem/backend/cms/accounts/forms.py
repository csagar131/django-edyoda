from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from accounts.models import Profile

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','password1','password2','first_name','last_name','email')


class UpdateProfileForm(forms.ModelForm):
    class meta:
        model = Profile
        fields = ('username','first_name','last_name')
