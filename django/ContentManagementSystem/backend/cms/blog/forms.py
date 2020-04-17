from django import forms
import re
from blog.models import Post
class ContactForm(forms.Form):

    countries = [('IND','INDIA'),('CHN','CHINA')]
    name = forms.CharField(max_length=50)
    email = forms.EmailField(required = False)
    phone = forms.RegexField(regex='^[6-9][0-9]{9}$',required = False)
    password = forms.CharField(max_length=50, widget = forms.PasswordInput)
    message = forms.CharField(max_length=500,widget=forms.Textarea)
    country = forms.ChoiceField(choices=countries)


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')

        if email == "" and phone == "":
            raise forms.ValidationError("atleast email or password should be provided")

    def clean_password(self):
        password = self.cleaned_data.get('password')
        m = re.search('[A-Z]',password)
        if not m:
            raise forms.ValidationError("password should contains atleast 1 uppercase")
        return password

class Search(forms.Form):
    search_blog = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'id':'searchbar'}))

class PostForm(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 26}))

    class Meta:
        model = Post
        fields = ['title','content','date','author_name','status','category','images']
