from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model= User #model that will be affected is user
        fields=['username','email','password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model= User #model that will be affected is user
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']