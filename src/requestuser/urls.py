from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import RequestUser, RequestUserList, RequestUserUpdate
urlpatterns = [


    path('requestuser/', RequestUser.as_view(
    ), name="request_user"),
    path('requestuserlist/', RequestUserList.as_view(
    ), name="request_user_list"),
    path('requestuserupdate/', RequestUserUpdate.as_view(
    ), name="request_user_update"),

]


