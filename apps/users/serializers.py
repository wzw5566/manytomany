# -*- coding: UTF-8 -*-
from django.contrib.auth import get_user_model
from apps.users.models import Role
from rest_framework import serializers

from rest_framework.validators import UniqueValidator

User = get_user_model()


class RoleSerializer(serializers.ModelSerializer):

    roles = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='role_name'
    )

    class Meta:
        model = Role
        fields = ("role_name", "role_desc", "role_parent_id")


class UserSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """

    class Meta:
        model = User
        fields = ("username", "password", "roles", "avatar")


