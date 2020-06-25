from django.urls import path
from dashboard.views import DashboardView, DashboardLikeView

urlpatterns = [

    path('', DashboardView.as_view(
    ), name="dashboard_view"),
    path('dashboardlikeview/', DashboardLikeView.as_view(
    ), name="dashboard_like_view")

]