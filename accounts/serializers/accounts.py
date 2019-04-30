from rest_framework import serializers

from ..models import Accounts


class AccountsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accounts
        fields = ("url", "slug", "title", "description", "created", "modified")
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}

    def create(self, validated_data):
        user = self.context['request'].user
        account = Accounts.objects.create(
            user=user, 
            **validated_data
        )
        return account
