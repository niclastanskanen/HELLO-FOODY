from django import forms
from django.forms import ModelForm
from customer.models import MenuItem


# Create a menu form
class MenuForm(ModelForm):
    class Meta:
        model = MenuItem
        fields = ('name', 'description', 'image', 'price', 'category', 'restaurant')
