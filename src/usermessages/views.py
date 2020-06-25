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
from .models import UserMessages
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from django.views import generic

#Post and get in a single view
class UserChatting(LoginRequiredMixin, generic.ListView):

    model = UserMessages
    template_name = 'usermessages/usermessages.html'

    def post(self, request, *args, **kwargs):
            print("33344444", kwargs['pk'], self.request.user.id)
            print("44444444", request.POST['message'])
    #         user_post_object = UserPosts.objects.filter(id=kwargs['pk'])
            user_message = UserMessages.objects.create(messagefrom=self.request.user.id, messageto=kwargs['pk'], messagetext=request.POST['message'], like_message=0)
    #         user_message.save()
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        """
        Return redirect url on success
        """
        return reverse('dashboard:dashboard_view')

    def get_queryset(self):
        from django.db.models import Q
        print("44440", self.kwargs.get('pk'))
        user_message_object_from = UserMessages.objects.filter((Q(messagefrom=self.request.user.id) & Q(messageto=self.kwargs.get('pk'))) | (Q(messagefrom=self.kwargs.get('pk')) & Q(messageto=self.request.user.id))).order_by('created_at')
        print("42", user_message_object_from)
        l = []
        for i in user_message_object_from:
            print("47", i.messagefrom)
            messagefrom = i.messagefrom
            from users.models import User
            user_object = User.objects.filter(id=messagefrom)
            d = dict()
            d["usermessage"]=i
            d["userobject"]=user_object[0]
            l.append(d)
        print("53", l)


        return l
        # user_message_object_to = UserMessages.objects.filter(messageto=self.request.user.id)
        # print("44", user_message_object_to)
        # comments_object = Comments.objects.filter(post=user_post_object[0])
        # print("77777774444", comments_object)
        # from users.models import User
        # print("53", self.request.user)
        # return comments_object