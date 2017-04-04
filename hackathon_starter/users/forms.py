from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile, HostRegistration


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class HostForm(forms.ModelForm):
    # username = forms.ForeignKey()
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(max_length=100)
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=30)
    zipcode = forms.CharField(max_length=15)
    country = forms.CharField(max_length=30)
    class Meta:
        model = HostRegistration
        fields = ['username', 'password', 'email', 'address', 'city', 'state', 'zipcode', 'country']
