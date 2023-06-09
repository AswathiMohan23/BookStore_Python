from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import BookModel
from book.serializer import BookSerializer


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

    def put(self, request):
        try:
            request.data.update({'user': request.user})
            book_data = BookModel.objects.get(id=request.data.get('id'))
            serializer = BookSerializer(book_data, request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "book list edited", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id):
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
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)
