from django.urls import path, re_path
from .reports import reporte_general, reporte_gestor

urlpatterns = [
    path('reporte_general/<int:report_id>/', reporte_general, name='reporte_general'),
    path('reporte_gestor/<int:gestor_id>/', reporte_gestor, name='reporte_gestor'),

]