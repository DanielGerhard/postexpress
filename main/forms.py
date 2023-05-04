from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import ClearableFileInput
from .models import Post


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password1"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', "description"]
        labels = {'title': 'titulo',
                  'description': ''}


class CustomClearableFileInput(ClearableFileInput):
    template_name = 'custom_clearable_file_input.html'


class MyForm(forms.Form):
    my_file_field = forms.FileField(widget=CustomClearableFileInput)
