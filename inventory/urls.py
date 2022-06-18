
from django.urls import path
from .views import(
    InventoryApiView,
    InventoryView,
    home
)

urlpatterns = [
    path('', home, name='home'),
    path('inventory', InventoryView.as_view(), name='“/inventory-view'),
    path('inventory/<int:id>', InventoryView.as_view(), name='“/inventory-view'),
    path('api/inventory', InventoryApiView.as_view(), name='inventory-api'),
    path('api/inventory/<int:id>', InventoryApiView.as_view(), name='inventory-api-id'),
]
