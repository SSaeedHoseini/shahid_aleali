from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.models import Group

from .serializers import GroupSerializer, UserSerializer, UserWithRolesSerializer, UserAvatarSerializer

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserWithRolesSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(methods=["PATCH"], detail=True, serializer_class=UserAvatarSerializer)
    def avatar(self, request, username):
        instance = self.get_object()
        serializer = UserAvatarSerializer(instance, data=request.data, partial=True, context={"request": request})
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class GroupViewSet(ListModelMixin, GenericViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
