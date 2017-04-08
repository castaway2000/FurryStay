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
    #no need for charfields here because we refrence the model with the fields
    class Meta:
        model = HostRegistration
        fields = ['address', 'city', 'state', 'zipcode', 'country']


# class UpdateProfile(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields ['interest', 'accomodation', 'about']