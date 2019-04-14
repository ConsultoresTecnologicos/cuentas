from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from djmoney.models.fields import MoneyField


class ItemAmounts(TimeStampedModel):
    """
    Account item amounts model for store amounts item of accounts
    fields:
    - amount
    - currency
    - created
    - modified
    - account_item
    """

    amount = MoneyField(
        max_digits=30, decimal_places=18, default_currency="USD"
    )
    account_item = models.ForeignKey(
        "AccountItems", on_delete=models.CASCADE, related_name="amounts"
    )

    class Meta:
        verbose_name = _("amount")
        verbose_name_plural = _("amounts")
        ordering = ("created", "account_item")

    def __str__(self):
        return str(self.amount)
