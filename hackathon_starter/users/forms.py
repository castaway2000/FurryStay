from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    email = forms.EmailField(max_length=100, required=True)
    address = forms.CharField(max_length=200, required=False)
    city = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=30, required=False)
    zipcode = forms.CharField(max_length=15, required=False)
    country = forms.CharField(max_length=30, required=False)
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'address', 'city',
                'state', 'zipcode', 'country']




#     password = forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

# class HostForm(forms.ModelForm):
#     username = forms.CharField(max_length=50, required=True)
#     password = forms.CharField(widget=forms.PasswordInput(), required=True)
#     email = forms.EmailField(max_length=100, required=True)
#     address = forms.CharField(max_length=200, required=False)
#     city = forms.CharField(max_length=100, required=False)
#     state = forms.CharField(max_length=30, required=False)
#     zipcode = forms.CharField(max_length=15, required=False)
#     country = forms.CharField(max_length=30, required=False)
#     class Meta:
#         model = HostRegistration
#         fields = ['username', 'password', 'email', 'address', 'city',
#             'state', 'zipcode', 'country']