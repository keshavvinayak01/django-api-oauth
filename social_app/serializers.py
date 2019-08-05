from rest_framework import serializers as sz
from .models import *
from django.utils import timezone

class UserSerializer(sz.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','is_superuser','first_name', 'last_name')

class ProfileSerializer(sz.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user.username', 'avatar', 'institute', 'age', 'bio')

class PostSerializer(sz.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','creator','title','description','input_file','output_file','created_at','likes','updated_at','published_date')
    
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.updated_at = timezone.now()
        instance.save()

        return instance

class CommentSerializer(sz.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'text', 'created_at')
    
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('title', instance.title)
        instance.updated_at = timezone.now()
        instance.save()
        
        return instance