"""django_poc2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
# from users.views import register

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('register/', register, name='register'),
    path('users/', include(('users.urls', 'user'), namespace='users'), ),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard'), ),
    path('userprofile/', include(('userprofile.urls', 'userprofile'), namespace='userprofile'), ),
    path('userlist/', include(('userlist.urls', 'userlist'), namespace='userlist'), ),
    path('viewprofile/', include(('viewprofile.urls', 'viewprofile'), namespace='viewprofile'), ),
    path('requestuser/', include(('requestuser.urls', 'requestuser'), namespace='requestuser'), ),
    path('followers/', include(('followers.urls', 'followers'), namespace='followers'), ),
    path('following/', include(('following.urls', 'following'), namespace='following'), ),
    path('userposts/', include(('userposts.urls', 'following'), namespace='userposts'), ),
    path('comments/', include(('comments.urls', 'comments'), namespace='comments'), ),
    path('usermessages/', include(('usermessages.urls', 'comments'), namespace='usermessages'), ),
    path('messagelist/', include(('messagelist.urls', 'comments'), namespace='messagelist'), ),

]

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
