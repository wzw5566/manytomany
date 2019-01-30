from django.shortcuts import render
from users.serializers import UserSerializer,RoleSerializer
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

#     def create(self, request, *args, **kwargs):
#         role = Role.objects.get(role_name="admin")
#         username = request.POST['username']
#         password = request.POST['password']
#         avatar = request.POST['avatar']
#
#         user = User(username=username, password=password, avatar=avatar)
#         user.save()
#         user.roles.add(role)
#         user.save()
#         return user
# #

class UserAIView(APIView):

    def get(self, request):
        user_list = User.objects.all()
        users = UserSerializer(user_list, many=True)
        return Response(users.data)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


