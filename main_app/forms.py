from django import forms
from .models import *
class SignUpForm(forms.Form):
    email = forms.EmailField(
        required=True,
    )
    username = forms.CharField(
        required=True,
    )
    password = forms.CharField(
        required=True,
    )
    password_validate = forms.CharField(
        required=True,
    )
    agree = forms.BooleanField(
        required=True,
    )


class ClipCreateForm(forms.Form):
    title = forms.CharField(
        required=True,
        initial='Username'
    )
    html= forms.CharField(
        widget=forms.Textarea(attrs={'rows':10}),
        required=True,
        )
    css = forms.CharField(
        widget=forms.Textarea(attrs={'rows':10}),
        required=True,
        )
    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Tag.objects.all(),
    )