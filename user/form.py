from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]


class UserUpdateform(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["email", "username"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
