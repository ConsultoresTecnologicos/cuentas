from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    fieldsets = (
        (None, {"fields": (User.USERNAME_FIELD, "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (User.USERNAME_FIELD, "password1", "password2"),
            },
        ),
    )
    list_display = (User.USERNAME_FIELD, "first_name", "last_name", "is_staff")
    search_fields = (User.USERNAME_FIELD, "first_name", "last_name")
    ordering = (User.USERNAME_FIELD,)
