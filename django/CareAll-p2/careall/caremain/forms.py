
from django import forms

class ActivateRequestForm(forms.Form):
    days = forms.CharField(widget = forms.TextInput(attrs={'readonly':False}))
