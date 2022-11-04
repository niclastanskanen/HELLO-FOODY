from django.db import models
from cloudinary.models import CloudinaryField


# Menu item that holds all of the fields for each individual
# menu item that will be on the website
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('menu_images')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.name


# Category model linked with menu element category with
# a main relationship. each category can have many menu items
# each item can have many categories
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# order model will store the order itself
# and any items connected to that order
# each menu item can have multiple order
# each order can have multiplemenu items
class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField(
        'MenuItem', related_name='order', blank=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'
