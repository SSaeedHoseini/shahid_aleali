from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

myUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = myUser
        fields = [
            "url",
            "first_name",
            "last_name",
            "national_code",
            "birthday",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        }


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = myUser
        fields = [
            "avatar",
        ]


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

    avatar_url = serializers.SerializerMethodField()

    def get_avatar_url(self, obj):
        res = obj.avatar
        if not res:
            return ""
        return obj.avatar.url

    class Meta:
        model = myUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "national_code",
            "birthday",
            "avatar_url",
            "user_groups",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        }
