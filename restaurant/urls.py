from django.urls import path
from restaurant.views import Dashboard, OrderDetails, AddMenu, EditMenu


urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('orders/<int:pk>/', OrderDetails.as_view(), name='order-details'),
    path('add/', AddMenu.as_view(), name='add-menu'),
    path('edit/', EditMenu.as_view(), name='edit-menu'),
]
