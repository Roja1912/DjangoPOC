from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from users.views import Register

urlpatterns = [


    path('register/', Register.as_view(
    ), name="register"),
    # path('login/', CustomLoginView.as_view(
    #     template_name='authentication/login.html'
    # ), name="login"),
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='authentication/logout.html'), name="logout"),

]


