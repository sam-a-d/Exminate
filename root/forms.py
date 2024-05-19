from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password = forms.PasswordInput()

