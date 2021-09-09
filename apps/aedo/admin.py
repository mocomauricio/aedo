from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Company, UserCompany, City, Delivery, Service

# Register your models here.
@register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'document', 'telephone', 'cellphone', 'address']
    ordering = ['name']
    search_fields = ['name', 'document']
    list_per_page = 50

@register(UserCompany)
class UserCompanyAdmin(admin.ModelAdmin):
    list_display = ['user', 'company']
    ordering = ['id']
    list_per_page = 50
    autocomplete_fields = ['user', 'company']

@register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'service_amount', 'employee_amount', 'aedo_amount']
    ordering = ['name']
    search_fields = ['name']
    list_per_page = 50

@register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['description']
    ordering = ['id']
    search_fields = ['description']
    list_per_page = 50


@register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'js/admin_delivery.js',      
        )

    list_display = ['id', 'company', 'employee', 'city', 'package', 'state', 'state2', 'total', 'pendiente']
    list_filter = ['state', 'state2']
    ordering = ['-id']
    search_fields = ['package', 'comment']
    list_per_page = 50
    autocomplete_fields = ['company', 'employee']

    @admin.display(empty_value='???')
    def total(self, obj):
        return obj.get_total()

    @admin.display(empty_value='???')
    def pendiente(self, obj):
        return obj.get_pending()