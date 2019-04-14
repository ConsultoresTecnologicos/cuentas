import factory


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.LazyAttribute(
        lambda o: "{}.{}@mailinator.com".format(
            o.first_name, o.last_name
        ).lower()
    )
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    class Meta:
        model = "users.User"
