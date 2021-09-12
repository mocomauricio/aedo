from django.urls import path, include
from rest_framework import routers
from .views import CityViewSet, DeliveryViewSet, DeliveryPendingViewSet, DeliveryVoteViewSet


router = routers.DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'deliveries', DeliveryViewSet)
router.register(r'pending-deliveries', DeliveryPendingViewSet)
router.register(r'vote', DeliveryVoteViewSet)

urlpatterns =  [

	path('', include(router.urls))
]