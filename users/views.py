from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.views import APIView
from users.serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny
from users.models import User
from decouple import config


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Return user data
class UserView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        # Get user token from request header
        user_token = request.headers.get("Authorization").split(" ")[1]
        # Get user data from token
        user_data = TokenBackend(algorithm="HS512").decode(user_token, config("SECRET_KEY"))
        print(user_data)
        # Get user from database
        # user = User.objects.get(id=user_data["user_id"])
        # Return user data
        return Response("user")
