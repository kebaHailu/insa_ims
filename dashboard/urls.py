from django.urls import path
from . import views 

urlpatterns = [
    path('dashboard/',views.index, name='dashboard-index'),
    path('staff/',views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/',views.staff_view, name='dashboard-staff-view'),
    path('products/',views.products, name='dashboard-products'),
    path('orders/',views.orders, name='dashboard-orders'),
    path('products/delete/<int:pk>/',views.product_delete, name='dashboard-product-delete'),
    path('products/update/<int:pk>/',views.product_update, name='dashboard-product-update'),
]