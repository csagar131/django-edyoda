from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    is_author = forms.BooleanField()
    class Meta:
        model = User
        fields = ('username','password1','password2','first_name','last_name','email','is_author')


class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name','last_name','email','bio','image','is_author')
