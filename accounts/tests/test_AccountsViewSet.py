import datetime

from django.urls import reverse
from django.utils import timezone

from rest_framework.test import APITestCase
from rest_framework import status
from oauth2_provider.models import get_application_model, AccessToken

from ..factories import AccountsFactory
from users.factories import UserFactory
from ..models import Accounts


Application = get_application_model()


class AccountsViewSetTest(APITestCase):
    def setUp(self):
        self.user = UserFactory.create(
            email="alviarez.leonardo@gmail.com", password="secret"
        )
        self.application = Application(
            name="Test Application",
            redirect_uris="http://localhost",
            user=self.user,
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_PASSWORD,
        )
        self.application.save()

        self.token = AccessToken.objects.create(
            user=self.user,
            token="1234567890",
            application=self.application,
            expires=timezone.now() + datetime.timedelta(days=1),
            scope="read write",
        )

        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(self.token.token)
        )

        self.url_list = reverse("accounts-list")
        self.accounts_data = AccountsFactory.create_batch(size=10)
        self.return_fields = (
            "url",
            "slug",
            "title",
            "description",
            "created",
            "modified",
        )

    def test_list_accounts(self):
        """
        Test get list accounts from API
        """
        response = self.client.get(self.url_list)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for account in response.data:
            self.assertListEqual(
                sorted(account.keys()), sorted(self.return_fields)
            )

    def test_retrieve_account(self):
        """
        Test get single account from API
        """
        account = AccountsFactory.create()
        url_detail = reverse("accounts-detail", args=(account.slug,))
        response = self.client.get(url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual(
            sorted(response.data.keys()), sorted(self.return_fields)
        )
        self.assertEqual(response.data["title"], account.title)
        self.assertEqual(response.data["slug"], account.slug)

    def test_create_account(self):
        """
        Test create new account from API
        """
        data = {
            "title": "The first account",
            "description": "This is the first account created on test",
        }
        response = self.client.post(self.url_list, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        account = Accounts.objects.all().last()
        self.assertEqual(response.data["slug"], account.slug)
