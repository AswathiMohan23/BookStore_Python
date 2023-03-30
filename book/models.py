from django.db import models

from user.models import UserModel


class BookModel(models.Model):
    book_name = models.CharField(max_length=150)
    description = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        db_table = "book"

    def __str__(self):
        return str(self.book_name)


class CartModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = "cart_table"


class CartItemModel(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE, related_name='cart_items')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.IntegerField()
