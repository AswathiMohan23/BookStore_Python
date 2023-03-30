from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import BookModel, CartModel
from book.serializer import BookSerializer, CartSerializer


class BookOperations(APIView):
    serializer_class = BookSerializer

    def post(self, request):
        try:
            request.data.update({'user': request.user})
            serializer = BookSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "book added", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            book_data = BookModel.objects.all()
            serializer = BookSerializer(book_data, many=True)
            return Response({"message": "list of books displayed", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)


class CartViews(APIView):
    def post(self, request):
        try:
            request.data.update({'user': request.user})
            cart_data=CartModel.objects.get(id=user.id,request=request.user)
            print(cart_data.data)
            serializer = CartSerializer(request.data,cart_data)
            # print(serializer.data)
            serializer.is_valid(raise_exception=True)
            return Response({"message": "book added to cart", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)
