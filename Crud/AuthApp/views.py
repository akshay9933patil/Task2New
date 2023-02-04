from .serializers import UserRegisterSerializer, UserModel
from rest_framework.generics import CreateAPIView


class UserRegisterAPI(CreateAPIView):
    serializer_class = UserRegisterSerializer
    