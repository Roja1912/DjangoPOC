
from django.views.generic.edit import SingleObjectMixin
from .models import UserRequesting
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import RequestSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView
from django.views.generic import ListView, TemplateView, DetailView, \
    UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from userprofile.models import Profiles
from rest_framework.response import Response

#1.add data into models coming from templates using serializer 2.add data to table using post
class RequestUser(SingleObjectMixin, CreateAPIView):

    model = UserRequesting
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
            print("1111115555555555", self.request.data)
            print("188888888888888888idddddd", int(self.request.data['requesting_user_id']))
            print("17777777777777777tyyyype", type(int(self.request.data['requesting_user_id'])))
            print("1999999999user", self.request.user.id)
            if not UserRequesting.objects.filter(user=self.request.user, request_id=int(self.request.data['requesting_user_id'])):
               # UserRequesting.objects.filter(user=self.request.user, request_id=int(self.request.data['requesting_user_id'])).update(accept=False)
            # else:
                print("3399999999")
                request_user = UserRequesting(user=self.request.user, request_id=int(self.request.data['requesting_user_id']))
                request_user.save()
            return Response("success")



#1.getting data from serializer  2.get a list of data directly from database
class RequestUserList(LoginRequiredMixin, ListView):
    model = UserRequesting
    template_name = 'requestuser/requestuser.html'

    # def get_queryset(self):
        # serializer = RequestSerializer.get_data(self)
        # return serializer

    def get_queryset(self):
        userrequestingobject = UserRequesting.objects.filter(request_id=self.request.user.id, accept=False)
        print("56", type(userrequestingobject[0].created_at))
        import time,datetime

        import datetime
        now = datetime.datetime.now()
        print("62", now)
        conv = datetime.datetime.strptime(str(now), "%Y-%m-%d %H:%M:%S.%f").strftime("%b %d %Y %H:%M%p")
        print("59", conv)

        from datetime import date, time
        date = date(2018, 7, 21)
        time = time(12, 45)
        nnow = datetime.datetime.combine(date, time)
        print("69", nnow)
        nconv = datetime.datetime.strptime(str(nnow), "%Y-%m-%d %H:%M:%S").strftime("%b %d %Y %H:%M%p")
        print("59", nconv)


        l=[]
        for each in userrequestingobject:
            from userprofile.models import Profiles
            profilesobject = Profiles.objects.filter(user=each.user)
            l.append(profilesobject)
        return l



#update a model object value
class RequestUserUpdate(SingleObjectMixin, UpdateAPIView):

    model = UserRequesting
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request, *args, **kwargs):
            from users.models import User
            user_object = User.objects.get(id=int(self.request.data['accepting_user_id']))
            print("77", user_object)
            UserRequesting.objects.filter(user=user_object, request_id=self.request.user.id).update(accept=True)
            from followers.models import Followers
            if Followers.objects.filter(user=self.request.user, followers_id=int(self.request.data['accepting_user_id'])):
                Followers.objects.filter(user=self.request.user,
                                         followers_id=int(self.request.data['accepting_user_id'])).update(remove=False)
            else:
                followers_object = Followers.objects.create(user=self.request.user, followers_id=int(self.request.data['accepting_user_id']))
                followers_object.save()
            from following.models import Following
            from users.models import User
            from userprofile.models import Profiles
            z = User.objects.get(id=int(self.request.data['accepting_user_id']))
            print("88888880", type(z))
            if Following.objects.filter(user=z, following_id=self.request.user.id):
                Following.objects.filter(user=z, following_id=self.request.user.id).update(unfollow=False)
            else:
                following_object = Following.objects.create(user=z, following_id=self.request.user.id)
                following_object.save()
            Profiles.objects.filter()
            return Response("success")

