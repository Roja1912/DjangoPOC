from .models import Following
from django.views.generic.edit import SingleObjectMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView
from django.views.generic import ListView, TemplateView, DetailView, \
    UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response

#get a list of data directly from database
class FollowingList(LoginRequiredMixin, ListView):
    model = Following
    template_name = 'following/following.html'

    # def get(self, request, *args, **kwargs):
    #     u = request.user
    #     if not u.is_staff:
    #         return HttpResponseForbidden()
    #     return super(UserList, self).get(request, *args, **kwargs)

    def get_queryset(self):
        from userprofile.models import Profiles
        print("11118888", Following.objects.filter(user=self.request.user))
        following_object = Following.objects.filter(user=self.request.user, unfollow=False)
        l = []
        for each in following_object:
            print("28", Profiles.objects.filter(user=each.following_id))
            l.append(Profiles.objects.filter(user=each.following_id))
        print(l)
        return l

    # def get_context_data(self, **kwargs):
    #     context = super(UserList, self).get_context_data(**kwargs)
    #     context['page_header'] = 'Clients'
    #     context['navigation'] = OrderedDict()
    #     context['navigation']['Emerald'] = reverse('dashboard:dashboard_view')
    #     context['navigation']['Clients'] = reverse('clients:client_list')
    #     return context

class FollowingUpdate(SingleObjectMixin, UpdateAPIView):

    model = Following
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request, *args, **kwargs):
            print("55555000000", self.request.data)
            from users.models import User
            from followers.models import Followers
            from requestuser.models import UserRequesting
            user_object = User.objects.get(id=int(self.request.data["unfollow_user_id"]))
            # print("77", user_object)
            Following.objects.filter(user=self.request.user, following_id=int(self.request.data["unfollow_user_id"])).update(unfollow=True)
            Followers.objects.filter(user=user_object, followers_id=self.request.user.id).update(remove=True)
            UserRequesting.objects.filter(user=self.request.user, request_id=int(self.request.data["unfollow_user_id"])).update(accept=False)
            return Response("success")



