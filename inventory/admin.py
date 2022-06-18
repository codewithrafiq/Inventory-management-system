from django.contrib import admin
from .models import *


admin.AdminSite.site_header = 'Inventory Administration'
admin.AdminSite.site_title = 'Inventory Administration'
admin.AdminSite.index_title = 'Inventory Administration'


class InventoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description', 'note',
                    'stock', 'availability', 'supplier']
    list_filter = ['name', 'availability', 'supplier']
    search_fields = ['name', 'description', 'note']
    ordering = ['name']
    
    list_per_page = 10





class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Supplier, SupplierAdmin)
