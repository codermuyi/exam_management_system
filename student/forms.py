from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . import models


class UpdateUserForm(UserChangeForm):
    class Meta:
       model = User
       fields = ['username', 'email', 'first_name', 'last_name']


class StudentUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['department', 'level', 'address', 'mobile', 'profile_pic']

