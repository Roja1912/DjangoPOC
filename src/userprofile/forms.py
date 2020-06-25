from django import forms
from .models import Profiles


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ['profile', 'blog']