from django.urls import path
from .views import PostsComments
from .views import CommentLikeView

urlpatterns = [


    path('postcomments/<int:pk>/', PostsComments.as_view(
    ), name="post_comments"),
    # path('postcommentslistview/<int:pk>/', PostsCommentsListView.as_view(
    # ), name="post_comments_list_view"),
    path('commentlikeview/', CommentLikeView.as_view(
    ), name="comment_like_view")


]