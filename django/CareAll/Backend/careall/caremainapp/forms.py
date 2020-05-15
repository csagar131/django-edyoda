from django import forms


class ReviewForm(forms.Form):
    review = forms.CharField()

    def clean(self):
        print(self.__dict__)

        


