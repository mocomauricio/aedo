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
    action = serializers.CharField(read_only=True)
    class Meta:
        model = Delivery
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['company'] = instance.company.name
        representation['employee'] = '<div><img class="img-fluid" src="%s"  width="100" height="100"></div><p>%s</p>' % (instance.employee.photo.url, instance.employee.get_full_name()) if (instance.employee) != None else "A definir"
        representation['reception_date'] = '%s %s' % (instance.reception_date.strftime("%d/%m/%Y"), instance.reception_time.strftime("%H:%M")), 
        representation['deliver_date'] = '%s %s' % (instance.deliver_date.strftime("%d/%m/%Y"), instance.deliver_time.strftime("%H:%M")), 
        representation['total'] = instance.get_total()
        representation['state'] = instance.get_state_display()
        representation['pending'] = instance.get_pending()
        representation['action'] = '<button class="btn btn-warning btn-sm" onclick="update_delivery(%d,%d,%d);">Editar</button>' % (instance.id, instance.state, instance.received)
        return representation
