"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.enable_nav_sidebar = False
admin.site.site_header = 'AEDO Entregas'

urlpatterns = [
    path('admin/', admin.site.urls),

    # aedo
    path('aedo/', include("apps.aedo.urls")),

    # incluimos las urls de nuestro sitio custom  
    path('', include("apps.homepage.urls")),

    # PWA
    path('', include("pwa.urls")),

    # api rest
    path('api/', include("apps.aedo.routes")),
    path('api/', include("apps.accounts.routes")),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
