from django.shortcuts import render

# Create your views here.


from following.models import Following
from userposts.models import UserPosts


from django.views.generic.edit import SingleObjectMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView
from django.views.generic import ListView, TemplateView, DetailView, \
    UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from .forms import CommentForm
from .models import Comments
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from django.views import generic

#Post and get in a single view
class PostsComments(LoginRequiredMixin, generic.ListView):

    model = UserPosts
    template_name = 'comments/comments.html'

    def post(self, request, *args, **kwargs):
            print("33344444", kwargs['pk'])
            print("44444444", request.POST['comments'])
            user_post_object = UserPosts.objects.filter(id=kwargs['pk'])
            user_profile = Comments.objects.create(post=user_post_object[0], comments=request.POST['comments'], like_comments=0, user=self.request.user)
            user_profile.save()
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        """
        Return redirect url on success
        """
        return reverse('dashboard:dashboard_view')

    def get_queryset(self):
        print("8888884444", self.kwargs.get('pk'))
        user_post_object = UserPosts.objects.filter(id=self.kwargs.get('pk'))
        comments_object = Comments.objects.filter(post=user_post_object[0])
        print("77777774444", comments_object)
        from users.models import User
        print("53", self.request.user)
        return comments_object

    # def get(self, request, *args, **kwargs):
    #      print("77777777777777", self.kwargs.get('pk'))
    #      user_post_object = UserPosts.objects.filter(id=self.kwargs.get('pk'))
    #      self.object = Comments.objects.filter(post=user_post_object[0])
    #      print("77777774444", self.object)
    #      # return self.object
    #      return super(PostsComments, self).get(request, *args, **kwargs)












# class PostsComments(SingleObjectMixin, CreateAPIView):
#
#     model = UserPosts
#     permission_classes = [IsAuthenticated, ]
#     authentication_classes = [TokenAuthentication, ]
#     template_name = 'comments/comments.html'
#
#
#     def post(self, request, *args, **kwargs):
#         print("66666999999999")




# class PostsCommentsListView(LoginRequiredMixin, ListView):
#     model = Comments
#     template_name = 'comments/comments.html'
#
#     # def get_queryset(self):
#         # serializer = RequestSerializer.get_data(self)
#         # return serializer
#
#     def get_queryset(self):
#         print("122", self.kwargs.get('pk'))
#         print("123", Comments.objects.filter(post=self.kwargs.get('pk')))
#         return Comments.objects.filter(post=self.kwargs.get('pk'))



class CommentLikeView(SingleObjectMixin, CreateAPIView):

    model = UserPosts
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    # serializer_class = RequestSerializer

    # def perform_create(self,serializer):
    #     validate_data = dict()
    #     validate_data['user'] = self.request.user
    #     validate_data['request_id'] = int(self.request.data['requesting_user_id'])
    #     RequestSerializer.create(self, validated_data= validate_data)
    #     or
    #     # serializer.save(user=self.request.user, request_id=int(self.request.data['requesting_user_id']))

    def post(self, request, *args, **kwargs):
            comment_object = Comments.objects.filter(id=int(self.request.data['commentid']))
            likes_count = comment_object[0].like_comments
            if self.request.data['like'] == True:
                likes_count += 1
                Comments.objects.filter(id=int(self.request.data['commentid'])).update(like_comments=likes_count)
            else:
                likes_count += -1
                Comments.objects.filter(id=int(self.request.data['commentid'])).update(like_comments=likes_count)
            return Response("success")


