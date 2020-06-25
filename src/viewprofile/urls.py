from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import ViewProfile,ViewProfileDetail

urlpatterns = [


    path('viewprofile/', ViewProfile.as_view(
    ), name="view_profile"),
    path('viewprofiledetail/<int:pk>/', ViewProfileDetail.as_view(
    ), name="view_profile_detail"),
]


