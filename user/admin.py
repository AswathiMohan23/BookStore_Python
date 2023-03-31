from django.contrib import admin

from book.models import BookModel, CartModel
from user.models import UserModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(BookModel)
admin.site.register(CartModel)

