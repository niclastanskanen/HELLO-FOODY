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
