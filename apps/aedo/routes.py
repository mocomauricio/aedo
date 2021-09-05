from django.urls import path, include
from rest_framework import routers
from .views import CityViewSet, DeliveryViewSet, DeliveryPendingViewSet


router = routers.DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'deliveries', DeliveryViewSet)
router.register(r'pending-deliveries', DeliveryPendingViewSet)


urlpatterns =  [

	path('', include(router.urls))
]