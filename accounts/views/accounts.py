from rest_framework import viewsets
from rest_framework import mixins

from ..models import Accounts
from ..serializers import AccountsSerializer


class AccountsViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer
