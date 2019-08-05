from django.urls import path
from .views import *

urlpatterns = [
    path('users', FullUserView.as_view()),
    path('posts', FullPostsView.as_view()),
    path('posts/<post_id>', PostDetailView.as_view()),
    path('posts/create', PostCreateView.as_view()),
    path('<username>/posts', UserPostView.as_view),
    path('posts/<post_id>/comments', CommentsView.as_view()),
    path('posts/<post_id>/comments/<comment_id>', SingleCommentView.as_view())
]