from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'example@gmail.com'}))
    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Your First Name'}))
    last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Your Last Name'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['username'].widget.attrs['placeholder'] = 'Choose a username'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter a password'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'

        



