# Generated by Django 4.1.7 on 2023-03-29 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_cart_cartitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='book',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='cart',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItems',
        ),
    ]
