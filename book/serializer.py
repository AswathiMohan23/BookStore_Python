from rest_framework import serializers

from book.models import BookModel, CartModel, CartItems, OrderModel, OrderItems


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
    book_details = serializers.SerializerMethodField()

    class Meta:
        model = CartModel
        fields = ["id", "book_details", "user"]

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

    def get_book_details(self, obj):
        print(obj.book.all())
        dict_book = {}
        book_list = [dict_book.update({i.book_name: i.price}) for i in obj.book.all()]
        return dict_book


class OrderSerializer(serializers.ModelSerializer):
    book_details = serializers.SerializerMethodField()

    class Meta:
        model = OrderModel
        fields = ["address", "orderDate", "book", "user","book_details"]

    def create(self, validated_data):
        user = validated_data.get('user')
        cart_list = CartModel.objects.filter(user=user)
        if not cart_list.exists():
            raise Exception("cart not found")
        cart = cart_list.first()
        cartitems = CartItems.objects.filter(cart=cart)
        if cartitems.count()!=0:
            order = OrderModel.objects.create(user=user, address=self.initial_data.get('address'))
            [OrderItems.objects.update_or_create(book=i.books, order=order, defaults={'quantity': i.quantity}) for i in
             cartitems]
            cartitems.delete()
        else:
            raise Exception("cart does not exists or already ordered")
        return order

    def get_book_details(self, obj):
        print(obj.book.all())
        dict_book = {}
        book_list = [dict_book.update({i.book_name: i.price}) for i in obj.book.all()]
        return dict_book
