from django.contrib.auth.views import LoginView
from django.views.generic import ListView, TemplateView, DetailView, \
    UpdateView, CreateView, DeleteView
from rest_framework.views import APIView
from django.urls import reverse, \
    reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from .forms import CreateProfileForm
from .models import Profiles
from users.models import User
from django.shortcuts import get_object_or_404

User = get_user_model()


class UpdateProfile(UpdateView):
    """
    AgentAddForm create new agent
    """
    template_name = 'userprofile/update_profile.html'
    model = Profiles

    def get_object(self, *args, **kwargs):
        profile_object = get_object_or_404(Profiles, pk=self.kwargs['pk'])
        print("26", profile_object)
        return profile_object

    def get_form_class(self):
        """
        Return agent forms
        """
        print("2222222666666666666666666")
        return CreateProfileForm

    # get_absolute_url
    def get_success_url(self):
        """
        Return redirect url on success
        """
        return reverse('dashboard:dashboard_view')

class GetProfile(APIView):
    """
    AgentAddForm create new agent
    """
    template_name = 'userprofile/profile.html'
    model = Profiles

    def get_form_class(self):
        """
        Return agent forms
        """
        print("2222222666666666666666666")
        return CreateProfileForm

    def get_success_url(self):
        """
        Return redirect url on success
        """
        return reverse('dashboard:dashboard_view')


#create html form using forms also changing style of fields
class CreateProfile(CreateView):
    """
    AgentAddForm create new agent
    """
    template_name = 'userprofile/profile.html'
    model = Profiles

    def get_form_class(self):
        """
        Return agent forms
        """
        return CreateProfileForm

    def get_success_url(self):
        """
        Return redirect url on success
        """
        return reverse('dashboard:dashboard_view')

    def form_valid(self, form):
        """
        Validate forms entries
        :param form: forms values
        :return: redirect to success url
        """
        print("4444411111")
        print("7777111", form.cleaned_data)
        profile = form.cleaned_data['profile']
        blog = form.cleaned_data['blog']
        user_profile = Profiles.objects.create(user=self.request.user, profile=profile, blog=blog)
        user_profile.save()
        return HttpResponseRedirect(self.get_success_url())

    # def post(self, request, *args, **kwargs):
    #     print("7777777777775555555555555")
    #     print("777766", request.POST)
    #     form_class = self.get_form_class()
    #     print("7778888888", form_class)
    #     form = self.get_form(form_class)
    #     print("80000", form)
    #     return HttpResponseRedirect(self.get_success_url())




