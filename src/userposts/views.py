from django.views.generic import ListView, TemplateView, DetailView, \
    UpdateView, CreateView, DeleteView
from rest_framework.views import APIView
from django.urls import reverse, \
    reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from .forms import CreateUserPostForm
from .models import UserPosts


class CreateUserPost(CreateView):
    """
    AgentAddForm create new agent
    """
    template_name = 'userposts/userposts.html'
    model = UserPosts

    def get_form_class(self):
        """
        Return agent forms
        """
        return CreateUserPostForm

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
        postimage = form.cleaned_data['postimage']
        caption = form.cleaned_data['caption']
        user_post = UserPosts.objects.create(user=self.request.user, postimage=postimage, caption=caption, likes=0)
        # user_post.save()
        return HttpResponseRedirect(self.get_success_url())


from django.shortcuts import render

# Create your views here.
