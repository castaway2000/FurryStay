from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']# , 'description', 'interests', 'city']


class HostForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'address', 'city', 'country']
