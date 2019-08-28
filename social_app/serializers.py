from rest_framework import serializers as sz
from rest_framework.settings import api_settings
from .models import *
from algorithms.models import JobInfo
from django.utils import timezone
from django.contrib.auth.models import User

class GetFullUserSerializer(sz.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','is_superuser','first_name', 'last_name','profile')


class UserSerializerWithToken(sz.ModelSerializer):
    password = sz.CharField(write_only=True)
    token = sz.SerializerMethodField()

    def get_token(self, object):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(object)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'] 
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'first_name', 'last_name')

class ProfileSerializer(sz.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user.username', 'avatar', 'institute', 'age', 'bio')

    def update(self, instance, validated_data):
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.age = validated_data.get('age', instance.age)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.institute = validated_data.get('institute', instance.institute)        
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


class PostSerializer(sz.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','creator','title','description','input_file','output_file','created_at','likes','updated_at','published_date')
    
    def create(self, validated_data):
        post = Post.objects.create(
            creator = self.request.user,
            title = validated_data.get('title', 'No title provided'),
            description = validated_data.get('description', 'No description provided'),
            input_file = validated_data.get('input_file'),
            created_at = timezone.now(),
            updated_at = timezone.now()
        )
        post.save()
        get_file_name(post.document.url,post)
        JobInfo.objects.create(
            post = post,
            status = 'Started',
            created_at = timezone.now(),
            modified_at = timezone.now()
        )


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.updated_at = timezone.now()
        instance.save()

        return instance