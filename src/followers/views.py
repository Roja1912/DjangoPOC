
from .models import Followers
from following.models import Following
from django.views.generic.edit import SingleObjectMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView
from django.views.generic import ListView, TemplateView, DetailView, \
    UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response

#get a list of data directly from database
class FollowersList(LoginRequiredMixin, ListView):
    model = Followers
    template_name = 'followers/followers.html'

    # def get(self, request, *args, **kwargs):
    #     u = request.user
    #     if not u.is_staff:
    #         return HttpResponseForbidden()
    #     return super(UserList, self).get(request, *args, **kwargs)

    def get_queryset(self):
        from userprofile.models import Profiles
        print("11118888", Followers.objects.filter(user=self.request.user))
        followers_object = Followers.objects.filter(user=self.request.user, remove=False)
        l = []
        for each in followers_object:
            l.append(Profiles.objects.filter(user=each.followers_id))
        print(l)
        return l

    # def get_context_data(self, **kwargs):
    #     context = super(UserList, self).get_context_data(**kwargs)
    #     context['page_header'] = 'Clients'
    #     context['navigation'] = OrderedDict()
    #     context['navigation']['Emerald'] = reverse('dashboard:dashboard_view')
    #     context['navigation']['Clients'] = reverse('clients:client_list')
    #     return context


class FollowersUpdate(SingleObjectMixin, UpdateAPIView):

    model = Followers
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request, *args, **kwargs):
            print("55555000000", self.request.data)
            from users.models import User
            from requestuser.models import UserRequesting
            user_object = User.objects.get(id=int(self.request.data["remove_user_id"]))
            # print("77", user_object)
            Followers.objects.filter(user=self.request.user, followers_id=int(self.request.data["remove_user_id"])).update(remove=True)
            Following.objects.filter(user=user_object, following_id=self.request.user.id).update(unfollow=True)
            UserRequesting.objects.filter(user=int(self.request.data["remove_user_id"]), request_id=self.request.user.id).update(accept=False)
            return Response("success")



