from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UsersChangeForm, UsersCreationForm
from .models import User


@admin.register(User)
class UsersAdmin(auth_admin.UserAdmin):
    form = UsersChangeForm
    add_form = UsersCreationForm
    model = User
