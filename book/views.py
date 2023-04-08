import json
import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import BookModel, CartModel
from book.serializer import BookSerializer, CartSerializer, OrderSerializer
from logger import set_logger

logger = set_logger()


class BookOperations(APIView):
    serializer_class = BookSerializer

    def post(self, request):
        logging.info("book added")
        try:
            request.data.update({'user': request.user})
            serializer = BookSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "book added", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        logging.info("book details retrieved")
        try:
            book_data = BookModel.objects.all()
            serializer = BookSerializer(book_data, many=True)
            return Response({"message": "list of books displayed", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        logging.info("book edited")
        try:
            request.data.update({'user': request.user})
            book_data = BookModel.objects.get(id=request.data.get('id'))
            serializer = BookSerializer(book_data, request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "book list edited", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id):
        logging.info("book deleted")
        try:
            if request.user.is_superuser:
                book_data = BookModel.objects.get(id=book_id)
                book_data.delete()
                return Response({"message": "book deleted", "status": 200, "data": {}},
                                status=status.HTTP_200_OK)
            else:
                return Response({"message": "only admin have permission to delete the book", "status": 403, "data": {}},
                                status=status.HTTP_403_FORBIDDEN)

        except Exception as e:
            logging.exception(e)
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)


class CartViews(APIView):
    def post(self, request):
        logging.info("added to cart")
        try:
            request.data.update({'user': request.user.id})
            serializer = CartSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "book added to cart", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        logging.info("cart retrieved")
        try:
            cart_data = CartModel.objects.filter(user=request.user.id)
            serializer = CartSerializer(cart_data, many=True)
            return Response({"message": "cart displayed", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        logging.info("cart deleted")
        try:
            user_cart = CartModel.objects.get(
                user=request.user.id)  # each user will only be having one cart so can use user id to delete a  cart
            user_cart.delete()
            return Response({"message": "cart deleted", "status": 200, "data": {}},
                            status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)


class OrderViews(APIView):
    def post(self, request):
        logging.info("order placed")
        try:
            request.data.update({'user': request.user.id})
            serializer = OrderSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "cart added to order", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

