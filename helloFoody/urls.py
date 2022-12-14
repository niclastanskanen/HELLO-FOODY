"""helloFoody URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from customer import views
from django.conf import settings
from django.conf.urls.static import static
from customer.views import (
    Index,
    Restaurants,
    Profile,
    Cart,
    Order,
    OrderConfirmation,
    OrderPayConfirmation,
    Menu,
    MenuSearch,
    ContactForm,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('contact/', views.contact, name='contact'),
    path('restaurant/', include('restaurant.urls')),
    path('', Index.as_view(), name='index'),
    path('restaurants/', Restaurants.as_view(), name='restaurants'),
    path('menu/', Menu.as_view(), name='menu'),
    path('menu/search/', MenuSearch.as_view(), name='menu-search'),
    path('profile/', Profile.as_view(), name='profile'),
    path('cart/', Cart.as_view(), name='cart'),
    path('order/', Order.as_view(), name='order'),
    path('order-confirmation/<int:pk>', OrderConfirmation.as_view(),
         name='order-confirmation'),
    path('payment-confirmation/', OrderPayConfirmation.as_view(),
         name='payment-confirmation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
