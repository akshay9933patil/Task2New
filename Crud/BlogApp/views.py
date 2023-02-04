from django.shortcuts import render
from .serializers import BlogSerializer, BlogModel
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class BlogCreateAPIView(APIView):
    
    def get(self, request):
        obj = BlogModel.objects.all()
        serializer = BlogSerializer(obj, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data, context=request)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)


class BlogGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
