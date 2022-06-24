from decouple import config
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.backends import TokenBackend

from users.models import User
from users.serializers import RegisterUserSerializer, UserSerializer


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Decode token from request headers and get user id
class UserView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):
        try:
            access_token = request.headers.get('Authorization').split(' ')[1]
        except AttributeError:
            return Response({"message": "Unable to authorize"}, status.HTTP_400_BAD_REQUEST)

        data = TokenBackend(algorithm='HS512', signing_key=config('SECRET_KEY')).decode(access_token)
        user = User.objects.filter(id=data.get('user_id')).first()

        if user:
            user_data = UserSerializer(user)
            return Response(user_data.data)

        return Response({"message": "Unable to authorize"}, status=status.HTTP_400_BAD_REQUEST)
