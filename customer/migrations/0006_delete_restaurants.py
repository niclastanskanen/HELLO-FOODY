# Generated by Django 4.1.3 on 2022-11-07 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_restaurants'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Restaurants',
        ),
    ]
