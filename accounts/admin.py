from django.contrib import admin

from .models import Accounts


@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "modified", "user")
