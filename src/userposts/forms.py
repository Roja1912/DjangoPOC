from django import forms
from .models import UserPosts


class CreateUserPostForm(forms.ModelForm):
    class Meta:
        print("7777777777")
        model = UserPosts
        fields = ['postimage', 'caption']