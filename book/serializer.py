from rest_framework import serializers

from book.models import BookModel


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ["id","book_name", "description", "author", "price", "quantity"]

    def validate(self,attrs):
        if self.initial_data["user"].is_superuser:
            return super().validate(attrs)
        raise Exception("user is not an admin")
