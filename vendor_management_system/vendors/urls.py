from django.urls import path
from .views import vendor_list, vendor_detail,purchase_order_list,purchase_order_detail, vendor_performance

urlpatterns = [
    path('api/vendors/', vendor_list),
    path('api/vendors/<int:vendor_id>/', vendor_detail),
     path('api/purchase_orders/', purchase_order_list),
    path('api/purchase_orders/<int:po_id>/', purchase_order_detail),
     path('api/vendors/<int:vendor_id>/performance/', vendor_performance),
]
