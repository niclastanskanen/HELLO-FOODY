from django.shortcuts import render
from django.views import View


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')


class Restaurants(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/restaurants.html')


class Search(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/search.html')


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/login.html')


class Cart(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/cart.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        starters = MenuItem.objects.filter(category__name__contains='Starters')
        main = MenuItem.objects.filter(category__name__contains='Main')
        desserts = MenuItem.objects.filter(category__name__contains='Desserts')
        drinks = MenuItem.objects.filter(category__name__contains='Drinks')

        # pass into context
        context = {
            'starters': starters,
            'main': main,
            'desserts': desserts,
            'drinks': drinks,
        }

        # render the template
        return render(request, 'customer/order.html', context)
