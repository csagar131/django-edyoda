from django import forms

class ContactForm(forms.Form):

    countries = [('IND','INDIA'),('CHN','CHINA')]

    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.RegexField(regex='^[6-9][0-9]{9}$')
    message = forms.CharField(max_length=500)
    country = forms.ChoiceField(choices=countries)
