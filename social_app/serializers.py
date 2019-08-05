from rest_framework import serializers as sz
from .models import *

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


class CommentSerializer(sz.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'text', 'created_at')