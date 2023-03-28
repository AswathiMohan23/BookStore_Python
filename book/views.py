from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from book.serializer import BookSerializer


class BookOperations(APIView):
    serializer_class = BookSerializer

    def post(self, request):
        try:
            request.data.update({'user': request.user})
            if request.user.is_superuser:
                print(request.user)
                print(request.data)
                serializer = BookSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({"message": "book added", "status": 200, "data": serializer.data},
                                status=status.HTTP_200_OK)
            else:
                return Response({"message": "User need to be an admin user to add books", "status": 400, "data": {}},
                                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

