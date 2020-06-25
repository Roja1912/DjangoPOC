from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from usermessages.models import UserMessages
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from django.views import generic

#Post and get in a single view
class MessageList(LoginRequiredMixin, generic.ListView):

    model = UserMessages
    template_name = 'messagelist/messagelist.html'

    def get_success_url(self):
        """
        Return redirect url on success
        """
        return reverse('dashboard:dashboard_view')

    def get_queryset(self):
        from django.db.models import Q
        print("44440", self.kwargs.get('pk'))
        user_message_object_from = UserMessages.objects.filter(Q(messagefrom=self.request.user.id) | Q(messageto=self.request.user.id)).order_by('created_at')
        print("42", user_message_object_from)
        l = []
        for i in user_message_object_from:
        #     print("47", i.messagefrom)
            messagefrom = i.messagefrom
            messageto = i.messageto
            from users.models import User
            if not i.messagefrom == self.request.user.id:
                user_object = User.objects.filter(id=messagefrom)
                if user_object[0] not in l:
                    l.append(user_object[0])
            if not i.messageto == self.request.user.id:
                user_object = User.objects.filter(id=messageto)
                if user_object[0] not in l:
                    l.append(user_object[0])


        #     d = dict()
        #     d["usermessage"]=i
        #     d["userobject"]=user_object[0]
        print("53", l)
        return l
