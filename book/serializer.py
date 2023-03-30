from rest_framework import serializers

from book.models import BookModel, CartModel, CartItemModel


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ["id", "book_name", "description", "author", "price", "quantity"]
        read_only_fields = ["id", "status","book_name", "description", "author", "price"]


    def validate(self, attrs):
        if self.initial_data["user"].is_superuser:
            return super().validate(attrs)
        raise Exception("user is not an admin")


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItemModel
        fields = ["id", "price", "book", "user", "cart"]


class CartSerializer(serializers.ModelSerializer):
    cart_item = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = CartModel
        fields = ["id", "status", "user"]
        read_only_fields = ["id", "status"]

    def create(self, validated_data):
        user = validated_data.get('user')
        cart_list = CartModel.objects.filter(user_id=user.id, status=False)
        if len(cart_list) == 0:  # checking whether the cart_list is an empty dictionary
            cart_list = CartModel.objects.create(user_id=user.id)
            CartModel.status = True
        else:
            pass
        return cart_list
