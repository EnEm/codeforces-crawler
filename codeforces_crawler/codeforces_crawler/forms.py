from django import forms

class UserIDForm(forms.Form):
    user = forms.CharField(required=True)

class CompareIDForm(forms.Form):
    user1 = forms.CharField(required=True)
    user2 = forms.CharField(required=True)