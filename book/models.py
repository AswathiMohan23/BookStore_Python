from django.db import models

from BookStoreProject import settings
from user.models import UserModel


class BookModel(models.Model):
    book_name = models.CharField(max_length=150)
    description = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=True)

    class Meta:
        db_table = "book_table"

    def __str__(self):
        return self.book_name


class CartModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ManyToManyField(BookModel, related_name='carts', through='CartItems')

    class Meta:
        db_table = "cart_table"

    def __str__(self):
        return str(self.user.username) # foreign key user  gives user object using user object attributes can be accessed


class CartItems(models.Model):
    books = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = "item_table"

    def __str__(self):
        return str(self.cart)
