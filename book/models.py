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
