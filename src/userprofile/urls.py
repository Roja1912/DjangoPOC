from django.urls import path
from .views import CreateProfile
from .views import UpdateProfile
from .views import GetProfile

urlpatterns = [

    path('', CreateProfile.as_view(
    ), name="user_profile"),
    path('updateprofile/<int:pk>/', UpdateProfile.as_view(
    ), name="update_profile"),
    path('<int:pk>/', GetProfile.as_view(
    ), name="get_profile"),


]