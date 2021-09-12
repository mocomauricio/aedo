from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny
from django.db.models import Q

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin
from .permissions import IsOwnerOrReadOnly
from .serializers import CitySerializer, DeliverySerializer, DeliveryVoteSerializer
from .models import City, Delivery, UserCompany

# Create your views here.
class CityViewSet(ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [AllowAny]


class DeliveryViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.request.user.groups.filter(name='Gestores'):
            return self.queryset.filter(employee=self.request.user).order_by('-id')

        elif self.request.user.groups.filter(name='Clientes'):
            return self.queryset.filter(company__in=[i.company for i in UserCompany.objects.filter(user=self.request.user)]).order_by('-id')

        return self.queryset.none()

class DeliveryPendingViewSet(ReadOnlyModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.request.user.groups.filter(name='Gestores'):
            return self.queryset.filter(employee=self.request.user).exclude(Q(state=3) | Q(state=4)).order_by('-id')

        elif self.request.user.groups.filter(name='Clientes'):
            return self.queryset.filter(company__in=[i.company for i in UserCompany.objects.filter(user=self.request.user)]).exclude(Q(state=3) | Q(state=4)).order_by('-id')

        return self.queryset.none()



class DeliveryVoteViewSet(GenericViewSet, UpdateModelMixin):
    queryset = Delivery.objects.all()
    serializer_class = DeliveryVoteSerializer
    permission_classes = [AllowAny]


