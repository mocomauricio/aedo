from django.urls import path, include
from .views import UpdateProfileView, ChangePasswordView

urlpatterns =  [
    path('update-profile/', UpdateProfileView.as_view(), name='update-profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]