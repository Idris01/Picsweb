from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
  path("", RedirectView.as_view(url="index/")), 
  path("index/", views.index, name="index"),
  path("register/", views.register, name="register"), 
  path("profile/", views.profile, name="profile"), 
  path("login/", views.login_view, name="login"), 
  path("logout/", views.logout_view, name="logout"),
  path("upload/", views.upload_view, name="upload"), 
  ]