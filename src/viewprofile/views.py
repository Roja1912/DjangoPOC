from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, TemplateView, DetailView, \
    UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, \
    reverse_lazy
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from collections import OrderedDict
from userprofile.models import Profiles
from followers.models import Followers
from following.models import Following
from userposts.models import UserPosts


class ViewProfile(LoginRequiredMixin, ListView):
    model = Profiles
    template_name = 'viewprofile/viewprofile.html'

    # def get(self, request, *args, **kwargs):
    #     u = request.user
    #     if not u.is_staff:
    #         return HttpResponseForbidden()
    #     return super(UserList, self).get(request, *args, **kwargs)

    def get_queryset(self):
        profile = Profiles.objects.filter(user=self.request.user, deleted_at__isnull=True)
        followers_count = Followers.objects.filter(user=self.request.user, remove=False)
        print("32222", followers_count.count())
        following_count = Following.objects.filter(user=self.request.user, unfollow=False)
        print("33334444", following_count.count())
        print("2999", profile)
        user_posts = UserPosts.objects.filter(user=self.request.user)
        l=[]
        d={}
        d["profile"] = profile[0]
        d["followers_count"] = followers_count.count()
        d["following_count"] = following_count.count()
        d["user_posts"] = user_posts
        d["posts_count"] = user_posts.count()
        l.append(d)
        print("444422", l)
        return l

    # def get_context_data(self, **kwargs):
    #     context = super(UserList, self).get_context_data(**kwargs)
    #     context['page_header'] = 'Clients'
    #     context['navigation'] = OrderedDict()
    #     context['navigation']['Emerald'] = reverse('dashboard:dashboard_view')
    #     context['navigation']['Clients'] = reverse('clients:client_list')
    #     return context

class ViewProfileDetail(LoginRequiredMixin, DetailView):
    """
    IngestionDataView class returns ingestion details
    of given ingestion id
    """
    model = Profiles
    template_name = 'viewprofile/viewprofiledetail.html'
    # queryset = Profiles.objects.all()

    # def get(self, request, *args, **kwargs):
    #     print("633333333", kwargs['pk'])
    #     self.object = Profiles.objects.filter(user=kwargs['pk'], deleted_at__isnull=True)
    #     print("69", self.object)
    #     return super(ViewProfileDetail, self).get(request, *args, **kwargs)

    # def get_object(self, queryset=None):
    #     print("6666622")
    #     obj = super().get_object()
    #     print("666666", obj)
    #     # followers_count = Followers.objects.filter(user=profile.user, remove=False)
    #     # print("666888", followers_count)
    #     # following_count = Following.objects.filter(user=profile.user, unfollow=False)
    #     # print("777777000", following_count)
    #     # l = []
    #     # d = {}
    #     # d["profile"] = profile
    #     # d["followers_count"] = followers_count.count()
    #     # d["following_count"] = following_count.count()
    #     # d["status_code"] = 200
    #     # l.append(d)
    #     # print("444422", l)
    #     return obj



