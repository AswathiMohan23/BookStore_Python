from django.contrib import admin

from book.models import BookModel
from user.models import UserModel

# Register your models here.
admin.site.register(BookModel)
admin.site.register(UserModel)

