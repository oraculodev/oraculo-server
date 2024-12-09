from django.contrib.auth import forms

from .models import User


class UsersChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UsersCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm):
        fields = "__all__"
        model = User
