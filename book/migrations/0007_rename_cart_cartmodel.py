# Generated by Django 4.1.7 on 2023-03-31 08:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0006_cart_cartitems_remove_cartmodel_user_bookmodel_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='CartModel',
        ),
    ]
