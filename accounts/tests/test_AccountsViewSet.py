from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from ..factories import AccountsFactory


class AccountsViewSetTest(APITestCase):
    def setUp(self):
        self.url_list = reverse("accounts-list")
        self.accounts_data = AccountsFactory.create_batch(size=10)
        self.return_fields = (
            "url",
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
