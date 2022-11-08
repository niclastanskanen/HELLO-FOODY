from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from customer.models import OrderModel
from .forms import MenuForm


class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        # get the current date
        today = datetime.today()
        orders = OrderModel.objects.filter(
            created_on__year=today.year,
            created_on__month=today.month,
            created_on__day=today.day)

        # loop throught the orders and add the price value
        # check if order is not delivered
        undelivered_order = []
        total_revenue = 0
        for order in orders:
            total_revenue += order.price

            if not order.is_delivered:
                undelivered_order.append(order)

        # pass total number of orders and total revenue into template
        context = {
            'orders': undelivered_order,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }

        return render(request, 'restaurant/dashboard.html', context)

    # method to defined to validate if the user is allowed to view dashboard
    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()


# Order details for restaurang logged in
class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        context = {
            'order': order
        }

        return render(request, 'restaurant/order-details.html', context)

    def post(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        order.is_delivered = True
        order.save()

        context = {
            'order': order
        }

        return render(request, 'restaurant/order-details.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()


class AddMenu(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):

        form = MenuForm

        return render(request, 'restaurant/add-menu.html', {'form':form})

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()
