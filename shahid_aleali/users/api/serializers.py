from django.contrib.auth import get_user_model
from rest_framework import serializers

from shahid_aleali.users.models import User
from django.contrib.auth.models import Group


myUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = myUser
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        }


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            "id",
            "name",
        ]


class UserWithRolesSerializer(serializers.ModelSerializer):
    user_groups = serializers.SerializerMethodField()

    def get_user_groups(self, obj):
        return GroupSerializer(
            instance=Group.objects.filter(id__in=obj.groups.all()).all(), many=True, read_only=True
        ).data

    class Meta:
        model = myUser
        fields = ["username", "name", "url", "user_groups"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        }
