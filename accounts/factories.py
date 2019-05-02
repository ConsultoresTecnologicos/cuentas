import factory
from factory import fuzzy
import random

from users.factories import UserFactory
from .models import AccountItems


class AccountsFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("sentence")
    description = factory.Faker("text")
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = "accounts.Accounts"


def get_item_type():
    "Return a random type from available choices."
    choices = [x[0] for x in AccountItems.TYPES]
    return random.choice(choices)


class AccountItemsFactory(factory.django.DjangoModelFactory):
    description = factory.Faker("text")
    type = factory.LazyFunction(get_item_type)
    account = factory.SubFactory(AccountsFactory)

    class Meta:
        model = "accounts.AccountItems"


class ItemAmountsFactory(factory.django.DjangoModelFactory):
    amount = fuzzy.FuzzyFloat(0.1, 10)
    amount_currency = factory.Faker("currency_code")
    account_item = factory.SubFactory(AccountItemsFactory)

    class Meta:
        model = "accounts.ItemAmounts"
