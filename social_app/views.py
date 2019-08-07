from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from .models import Profile, Post, Comment
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer, GetFullUserSerializer, ProfileSerializer, PostSerializer, CommentSerializer
from .permissions import isOwnerOrReadOnly, isSuperUserOrReadOnly

class GetAllUserAndProfiles(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = GetFullUserSerializer
    permission_classes = [isSuperUserOrReadOnly]

class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        user = request.data.get('user')
        if not user:
            return Response({'response' : 'error', 'message' : 'No data found'})
        serializer = UserSerializer(data = user)
        if serializer.is_valid():
            saved_user = serializer.save()
        else:
            return Response({"response" : "error", "message" : serializer.errors})
        return Response({"response" : "success", "message" : "user created succesfully"})    

    
# replace by customized homepage 
class FullPostsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.filter(published = True)
    serializer_class = PostSerializer

class PostDetailView(APIView):
    permission_classes = [isOwnerOrReadOnly]

    def get(self, request, post_id):
        try : 
            post = Post.objects.get(id = post_id)
            if not post.published and request.user != post.creator:
                return Response({'response' : 'error', 'message' : "Not found"})
        except Exception as e:
            return Response({'response' : 'error', 'message' : str(e)})
        serializer = PostSerializer(post)
        return Response({ 'response' : 'success', 'post' : serializer.data })

    def delete(self, request, post_id):
        try : 
            post = Post.objects.get(id = post_id).delete()
        except Exception as e : 
            return Response({'response' : 'error', 'message' : str(e)})             
        return Response({'response' : 'success', 'message' :  'Post with id {} deleted'.format(post_id)})

# Call the algorithm here
class PostCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        post = request.data.get('post')
        if not post:
            return Response({'response' : 'error', 'message' : 'No data found'})
        serializer = PostSerializer(data = post)
        if serializer.is_valid():
            saved_post = serializer.save()
        else:
            return Response({"response" : "error", "message" : serializer.errors})
        return Response({"response" : "success", "message" : "post created succesfully at ".format(str(saved_comment.created_at))})

class UserPostView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, username):
        if request.user.username == username :
            posts = Post.objects.filter(creater__username = username)
        else:
            posts = Post.objects.filter(creater__username = username, published = True)
        if not posts:
            return Response({'response' : 'error', })
        serializer = PostSerializer(posts, many=True)
        return Response({'posts' : serializer.data})

class CommentsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, post_id):
        comments = Comment.objects.filter(post__id = post_id)
        if not comments : 
            return Response({'response' : 'error', 'message' : 'no comments found'})
        serializer = CommentSerializer(comments, many=True)
        return Response({'comments' : serializer.data})

    def post(self, request, post_id):
        comment = request.data.get('comment')
        serializer = CommentSerializer(data = comment)
        if serializer.is_valid():
            saved_comment = serializer.save()
        else:
            return Response({"response" : "error", "message" : serializer.errors})
        return Response({"response" : "success", "message" : "comment created succesfully at ".format(str(saved_comment.created_at))})

class SingleCommentView(APIView):
    permission_classes = [isOwnerOrReadOnly]
    def put(self, request, post_id, comment_id):
        try : 
            comment = Comment.objects.get(post__id = post_id, id = comment_id)
            data = request.data.get('comment')
            serializer = CommentSerializer(instance=comment, data=data, partial=True)
            if serializer.is_valid():
                comment = serializer.save()                
        except Exception as e : 
            return Response({'response' : 'error', 'message' : str(e)})
        return Response({'response' : "success", 'message' : "Comment-{} updated successfully".format(comment_saved.id)})

    def delete(self, request, post_id, comment_id):
        try : 
            comment = Comment.objects.get(post__id = post_id, id = comment_id).delete()
        except Exception as e : 
            return Response({'response' : 'error', 'message' : str(e)})
        return Response({'response' : 'success', 'message' : 'Removed comment on Post-{} with id : {}'.format(post_id, comment_id)})

class ProfileView(APIView):
    permission_classes = [isOwnerOrReadOnly]

    def get(self, request, username):
        profile = Profile.objects.get(user__username = username)
        if not profile : 
            return Response({'response' : 'error', 'message' : 'no such user'})
        serializer = ProfileSerializer(comments, many=True)
        return Response({'profile' : serializer.data})

    def put(self, request, username):
        try : 
            profile = Profile.objects.get(user__username = username)
            data = request.data.get('profile')
            serializer = ProfileSerializer(instance=comment, data=data, partial=True)
            if serializer.is_valid():
                profile = serializer.save()                
        except Exception as e : 
            return Response({'response' : 'error', 'message' : str(e)})
        return Response({'response' : "success", 'message' : "Profile : {} updated successfully".format(username)})