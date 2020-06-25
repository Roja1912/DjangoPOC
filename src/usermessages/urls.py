from django.urls import path
from .views import UserChatting

urlpatterns = [


    path('userchatting/<int:pk>/', UserChatting.as_view(
    ), name="user_chatting"),



]