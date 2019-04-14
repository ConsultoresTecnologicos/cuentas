from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class AccountItems(TimeStampedModel):
    """
    Account items model for store items of accounts
    fields:
    - description
    - type [debit, credit]
    - created
    - modified
    - account
    """

    DEBIT = "debit"
    CREDIT = "credit"
    TYPES = ((DEBIT, _("Debit")), (CREDIT, _("Credit")))

    description = models.TextField(_("description"), blank=True, null=True)
    type = models.CharField(max_length=6, choices=TYPES)
    account = models.ForeignKey(
        "Accounts", on_delete=models.CASCADE, related_name="items"
    )

    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")
        ordering = ("created", "account")

    def __str__(self):
        return self.description
