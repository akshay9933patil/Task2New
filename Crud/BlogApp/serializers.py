from rest_framework import serializers
from .models import BlogModel


class BlogSerializer(serializers.ModelSerializer):

    owner = serializers.CharField(read_only=True)
    
    class Meta:
        model = BlogModel
        fields = '__all__'

    def create(self, validated_data):
        User = self.context.get('request').user
        print('User************', User)
        validated_data.update({'owner': str(User)})
        return BlogModel.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.owner = validated_data.get('owner', instance.owner)
        return instance