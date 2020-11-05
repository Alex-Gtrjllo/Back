from django.urls import path, re_path

from Profile import views

urlpatterns = [
    re_path(r'^profileModel_url', views.ProfileModelView.as_view()),
    re_path(r'^profileUser_url', views.ProfileUserView.as_view()),
    re_path(r'^profileUserMethod_url/(?P<pk>[0-9]+)$', views.ProfileUserMethods.as_view())
    
]