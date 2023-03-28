from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializer import RegistrationSerializer, LoginSerializer


class UserRegistration(APIView):

    def post(self, request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Registration completed", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:

            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):

    serializer_class = LoginSerializer

    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data,context={'request':request})

            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "login successful", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

