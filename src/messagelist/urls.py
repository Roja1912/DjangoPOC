from django.urls import path
from .views import MessageList

urlpatterns = [


    path('messagelist/', MessageList.as_view(
    ), name="message_list"),



]