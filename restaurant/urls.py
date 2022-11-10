from django.urls import path
from restaurant.views import Dashboard, OrderDetails, AddMenu, EditMenu, EditItem
from . import views


urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('orders/<int:pk>/', OrderDetails.as_view(), name='order-details'),
    path('add/', AddMenu.as_view(), name='add-menu'),
    path('edit-menu/', EditMenu.as_view(), name='edit-menu'),
    path('edit-item/<int:pk>/', EditItem.as_view(), name='edit-item'),
]