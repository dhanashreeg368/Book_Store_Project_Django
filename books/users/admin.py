from django.contrib import admin
# The admin is a common place to
# manipulate user data and there is tight coupling between the built-in User and the
# admin
# Register your models here.


from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import UserChangeForm,UserCreationForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserCreationForm
    model = CustomUser
    list_display = ['email', 'username']


admin.site.register(CustomUser, CustomUserAdmin)
