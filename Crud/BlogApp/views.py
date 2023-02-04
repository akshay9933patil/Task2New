from django.shortcuts import render
from .serializers import BlogSerializer, BlogModel
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerPermission


class BlogCreateAPIView(APIView):

    serializer_class = BlogSerializer
    model_class = BlogModel
    permission_classes = [IsOwnerPermission]
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        fetched = self.model_class.objects.all()
        serializer = self.serializer_class(fetched, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)


class BlogGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()
    permission_classes = [IsOwnerPermission]
    authentication_classes = [JWTAuthentication]
