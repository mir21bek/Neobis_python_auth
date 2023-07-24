from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from users.forms import UserCreationsForm

User = get_user_model()


@admin.register(User)
class AdminUser(UserAdmin):
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2'),
                }),
    )
    add_form = UserCreationsForm
