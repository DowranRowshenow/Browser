from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('return/', views.ReturnPageView.as_view(), name="return"),
]