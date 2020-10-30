from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from auth_.models import MainUser


@admin.register(MainUser)
class MainUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active',)
