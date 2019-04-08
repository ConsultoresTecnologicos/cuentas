from django import forms
from django.contrib.auth.forms import (
    UserCreationForm as BaseUserCreationForm,
    UserChangeForm as BaseUserChangeForm,
)
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm):
        model = User
        fields = (User.USERNAME_FIELD,)
        field_classes = {User.USERNAME_FIELD: forms.EmailField}


class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = BaseUserChangeForm.Meta.fields
        field_classes = {User.USERNAME_FIELD: forms.EmailField}
