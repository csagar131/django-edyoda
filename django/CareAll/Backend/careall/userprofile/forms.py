from django import forms
from userprofile.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2','age','gender','image','address','Phone','is_elder')
    