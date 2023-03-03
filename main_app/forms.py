from django import forms
from .models import *


class SignUpForm(forms.Form):
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={'placeholder': 'email'})
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'username'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'username'})
    )
    password_validate = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'username'})
    )


class LogInForm(forms.Form):
    username = forms.CharField(
        required=True,
    )
    password = forms.CharField(
        required=True,
    )


class ClipCreateForm(forms.Form):
    title = forms.CharField(
        required=True,
    )
    html = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10}),
        required=True,
    )
    css = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10}),
        required=True,
    )
    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Tag.objects.all(),
    )
