# -*- coding: UTF-8 -*-
from django.contrib.auth import get_user_model
from apps.users.models import Role
from rest_framework import serializers

from rest_framework.validators import UniqueValidator

User = get_user_model()


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ("role_name", "role_desc", "role_parent_id")


class UserSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    # roles = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='role_name'
    # )

    # roles = RoleSerializer(many=True)

    class Meta:
        model = User
        fields = ("username", "password", "avatar", "roles")

    def create(self, validated_data):

        # user = super(UserSerializer, self).create(validated_data=validated_data)
        # user.set_password(validated_data["password"])
        print("validated_data", validated_data)
        roles_list = validated_data.pop('roles')
        print(roles_list)
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()

        for role in roles_list:
            new_role = Role.objects.filter(role_name=role.role_name).first()
            # new_role.save()
            user.roles.add(new_role)
            user.save()
        return user


