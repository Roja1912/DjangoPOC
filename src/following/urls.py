from django.urls import path
from .views import FollowingList, FollowingUpdate


urlpatterns = [

    path('followinglist', FollowingList.as_view(
    ), name="following_list"),
    path('followingupdate', FollowingUpdate.as_view(
    ), name="following_update"),

]