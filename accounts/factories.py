import factory

from users.factories import UserFactory


class AccountsFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("sentence")
    description = factory.Faker("text")
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = "accounts.Accounts"
