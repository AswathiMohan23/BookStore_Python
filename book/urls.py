from django.urls import path
from . import views

urlpatterns = [
    path('book', views.BookOperations.as_view(), name="book"),
    path('cart', views.CartViews.as_view(), name="cart"),
    path('book/<int:book_id>', views.BookOperations.as_view(), name='book'),
    path('order', views.OrderViews.as_view(), name="order"),
    path('order/<int:order_id>', views.OrderViews.as_view(), name='order'),

]
