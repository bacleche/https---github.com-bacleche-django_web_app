from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from blog.models import Post


from django.contrib.auth.forms import AuthenticationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'file', 'is_mp3', 'is_mp4', 'is_image']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'file', 'is_mp3', 'is_mp4', 'is_image']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

