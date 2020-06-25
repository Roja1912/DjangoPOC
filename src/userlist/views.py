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

#get a list of data directly from database
class UserList(LoginRequiredMixin, ListView):
    model = Profiles
    template_name = 'userlist/userlist.html'

    # def get(self, request, *args, **kwargs):
    #     u = request.user
    #     if not u.is_staff:
    #         return HttpResponseForbidden()
    #     return super(UserList, self).get(request, *args, **kwargs)

    def get_queryset(self):
        from  following.models import Following
        # following_object = Following.objects.filter(user=self.request.user.id)
        # print("26", following_object[0].following_id)
        # print("27", Profiles.objects.filter(deleted_at__isnull=True).exclude(user=self.request.user))
        profile_object = Profiles.objects.filter(deleted_at__isnull=True).exclude(user=self.request.user)
        l = []
        for each in profile_object:
            d = dict()
            d["profile_object"] = each
            following_object = Following.objects.filter(user=self.request.user.id, unfollow=False)
            if following_object:
                if following_object[0].following_id == each.user.id:
                    d["button"] = "Following"
                else:
                    d["button"] = "Send"
            else:
                d["button"] = "Send"
            l.append(d)
        print("38", l)
        return l

    # def get_context_data(self, **kwargs):
    #     context = super(UserList, self).get_context_data(**kwargs)
    #     context['page_header'] = 'Clients'
    #     context['navigation'] = OrderedDict()
    #     context['navigation']['Emerald'] = reverse('dashboard:dashboard_view')
    #     context['navigation']['Clients'] = reverse('clients:client_list')
    #     return context



