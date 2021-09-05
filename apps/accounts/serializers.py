from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    short_name = serializers.CharField(read_only = True)
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'photo', 'short_name']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['short_name'] = instance.get_short_name()
        return representation

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)