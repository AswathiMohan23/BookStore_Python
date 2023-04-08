from django.db import models

from BookStoreProject import settings
from user.models import UserModel


class BookModel(models.Model):
    book_name = models.CharField(max_length=150)
    description = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=True)

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
        return str(
            self.user.username)  # foreign key user  gives user object using user object attributes can be accessed


class CartItems(models.Model):
    books = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = "item_table"

    def __str__(self):
        return str(self.cart)


class OrderModel(models.Model):
    address = models.CharField(max_length=200)
    orderDate = models.DateTimeField(auto_now_add=True)
    book = models.ManyToManyField(BookModel, related_name='order', through='OrderItems')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = "order_table"


class OrderItems(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = "orderItems_table"
