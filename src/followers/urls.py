from django.urls import path
from .views import FollowersList, FollowersUpdate


urlpatterns = [

    path('followerslist', FollowersList.as_view(
    ), name="followers_list"),
    path('followersupdate', FollowersUpdate.as_view(
    ), name="followers_update"),

]