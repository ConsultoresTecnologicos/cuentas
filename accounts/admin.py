from django.contrib import admin

from .models import Accounts, AccountItems, ItemAmounts


@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "modified", "user")


@admin.register(AccountItems)
class AccountsItemsAdmin(admin.ModelAdmin):
    list_display = ("description", "created", "modified", "account")


@admin.register(ItemAmounts)
class ItemAmountsAdmin(admin.ModelAdmin):
    list_display = ("amount", "created", "modified", "account_item")
