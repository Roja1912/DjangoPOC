from django.contrib.auth.views import LoginView
from django.views.generic import ListView, TemplateView, DetailView, \
    UpdateView, CreateView, DeleteView
from django.urls import reverse, \
    reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from collections import OrderedDict
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


#Registartion using FBV using inbuilt user model
# def register(request):
#     from django.contrib import messages
#     from django.shortcuts import redirect
#     if request.method == "POST":
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            form.save()
#            username = form.cleaned_data.get('username')
#            # messages.success(request, f'Account created for {username}')
#            return redirect('users:login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'authentication/register.html', {'form': form})



#Registeration using CBV by swapping inbuilt user table with our definr user table in modles
class Register(CreateView):
    """
    AgentAddForm create new agent
    """
    template_name = 'authentication/register.html'

    def get_form_class(self):
        """
        Return agent forms
        """
        print("44444444444000000000000000")
        from .forms import ClientAgentForm
        return ClientAgentForm

    def get_success_url(self):
        """
        Return redirect url on success
        """
        return reverse('users:register')

    def form_valid(self, form):
        """
        Validate forms entries
        :param form: forms values
        :return: redirect to success url
        """
        print("5666666666666")
        password = form.cleaned_data['password1']
        print("61", password)
        self.object = form.save()
        print("6333")
        return HttpResponseRedirect(self.get_success_url())


# #Login using CBV
# class CustomLoginView(LoginView):
#     """
#     CustomLoginView class handle user login
#     """
#     template_name = 'authentication/login.html'
#     authentication_form = CustomLoginForm
