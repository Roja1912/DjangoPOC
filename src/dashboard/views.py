

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


#
# class DashboardView(View):
#     """
#         This is using views,it is an old method
#     """
#     def get(self, request, *args, **kwargs):
#         return render(request, "dashboard/dashboard.html")

#study about templateview
class DashboardView(LoginRequiredMixin, ListView):
    """
    DashboardView class returns dashboard template,this is new method using TemplateView
    """
    model = UserPosts
    template_name = 'dashboard/dashboard.html'
    #
    # def get_context_data(self, **kwargs):
    #     """
    #     Define various HTML elements for class template
    #     :param kwargs:
    #     :return: context dictionary
    #     """
    #     context = super(DashboardView, self).get_context_data(**kwargs)
    #     context['page_header'] = 'Dashboard'
    #     context['navigation'] = OrderedDict()
    #     context['navigation']['Emerald'] = reverse('dashboard:dashboard_view')
    #     return context

    def get_queryset(self):
        print("555577777")
        post_id_list = []
        following_object = Following.objects.filter(user=self.request.user, unfollow=False)
        print("6666660", following_object)
        for each_following_object in following_object:
            following_user_post = UserPosts.objects.filter(user=each_following_object.following_id)
            for each_following_user_post in following_user_post:
                post_id_list.append(each_following_user_post)
        userposts = UserPosts.objects.filter(user=self.request.user)
        for each in userposts:
            post_id_list.append(each)
        print("66677777777", post_id_list)
        return post_id_list


class DashboardLikeView(SingleObjectMixin, CreateAPIView):

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
            print("777777666666", self.request.data)
            print("188888888888888888idddddd", self.request.data['like'])
            user_post_object = UserPosts.objects.filter(id=int(self.request.data['postid']))
            print("7777777999999999", user_post_object[0].likes)
            likes_count = user_post_object[0].likes
            if self.request.data['like'] == True:
                likes_count += 1
                UserPosts.objects.filter(id=int(self.request.data['postid'])).update(likes=likes_count)
            else:
                likes_count += -1
                UserPosts.objects.filter(id=int(self.request.data['postid'])).update(likes=likes_count)

            print("1111188888888")
            return Response("success")



