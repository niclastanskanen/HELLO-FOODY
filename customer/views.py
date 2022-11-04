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

    # grab all the selected items
    # get menu item for that item thats selected
    # return name, price and id to show calculations price
    # then pass in the items and price to show in a template afterwards
    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

            for item in order_items['items']:
                price += item['price']
                item_ids.append(item['id'])

            order = OrderModel.objects.create(price=price)
            order.items.add(*item_ids)

            context = {
                'items': order_items['items'],
                'price': price
            }

            return render(request, 'customer/order_confirmation.html', context)
