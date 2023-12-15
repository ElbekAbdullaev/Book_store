from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Get the custom user model
CustomUser = get_user_model()

# Define the custom admin class for the custom user model
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']

# Register the custom user model with the custom admin class

admin.site.unregister(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)