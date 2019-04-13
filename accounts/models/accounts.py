from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import (TimeStampedModel,
                                         TitleSlugDescriptionModel)


class Accounts(TitleSlugDescriptionModel, TimeStampedModel):
    """
    Account model for store user accounts
    fields:
    - title
    - slug
    - description
    - created
    - modified
    - user
    """

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="accounts"
    )

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")
        ordering = ("created", "user")

    def __str__(self):
        return self.title
