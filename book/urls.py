from django.urls import path
from . import views

urlpatterns = [
    path('book', views.BookOperations.as_view(), name="book"),
    path('book/<int:book_id>', views.BookOperations.as_view(), name='book'),

]