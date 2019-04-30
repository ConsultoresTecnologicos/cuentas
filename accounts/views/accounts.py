from rest_framework import viewsets
from rest_framework import mixins

from ..models import Accounts
from ..serializers import AccountsSerializer

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope


class AccountsViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [TokenHasReadWriteScope]
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer
    lookup_field = "slug"
