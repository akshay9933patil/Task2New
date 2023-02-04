from rest_framework import serializers
from .models import BlogModel


class BlogSerializer(serializers.ModelSerializer):

    # owner = serializers.CharField(read_only=True)
    
    class Meta:
        model = BlogModel
        fields = '__all__'