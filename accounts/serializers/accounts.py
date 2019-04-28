from rest_framework import serializers

from ..models import Accounts


class AccountsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accounts
        fields = ("url", "title", "description", "created", "modified")
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
