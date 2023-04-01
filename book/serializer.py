from rest_framework import serializers

from book.models import BookModel, CartModel, CartItems


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ["id", "book_name", "description", "author", "price", "quantity", "user"]
        read_only_fields = ["id", "user"]

    def validate(self, attrs):
        if self.initial_data["user"].is_superuser:
            return super().validate(attrs)
        raise Exception("user is not an admin")


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ['id', 'cart', 'books', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = ["id", "book", "user"]

    def create(self, validated_data):
        user = validated_data.get('user')

        cart_list = CartModel.objects.filter(user=user)
        if not cart_list.exists():
            cart = CartModel.objects.create(user=user)
        else:
            cart = cart_list.first()  # returns the first item of an object.
        book = BookModel.objects.get(id=self.initial_data.get('book'))

        CartItems.objects.update_or_create(books=book, cart=cart,
                                           defaults={'quantity': self.initial_data.get('quantity')})
        return cart
