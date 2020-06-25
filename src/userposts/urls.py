from django.urls import path
from .views import CreateUserPost

urlpatterns = [

    path('', CreateUserPost.as_view(
    ), name="create_user_post"),

]