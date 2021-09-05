from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import login, authenticate
from rest_framework.response import Response

from rest_framework import status
from rest_framework import generics

from django.contrib.auth import get_user_model

from .serializers import UserSerializer, ChangePasswordSerializer
from .permissions import IsMyUser

User = get_user_model()

class UpdateProfileView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    model = User
    permission_classes = (IsMyUser,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            username = self.request.user.email
            new_password = serializer.data.get("new_password")
            
            self.object.set_password(new_password)
            self.object.save()

            user = authenticate(username=username, password=new_password)
            login(request, user)

            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

