from django.conf import settings
from rest_framework import serializers
from .models import City, Delivery


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    total = serializers.IntegerField(read_only = True)
    pending = serializers.IntegerField(read_only = True)
    class Meta:
        model = Delivery
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['total'] = instance.get_total()
        representation['state'] = instance.get_state_display()
        representation['pending'] = instance.get_pending()
        return representation
