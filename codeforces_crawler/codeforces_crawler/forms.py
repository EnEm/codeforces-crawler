from django import forms

class UserIDForm(forms.Form):
    user = forms.CharField(required=True)