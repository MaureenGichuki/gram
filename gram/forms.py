from django import forms
from .models import Profile, Post, Comment

class DetsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_pic", "bio"]

class PostsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["pic", "caption"]

class comments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]