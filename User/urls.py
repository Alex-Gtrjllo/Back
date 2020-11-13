from django.urls import path, re_path

from User import views

urlpatterns = [
    re_path(r'^User_url', views.UserModelView.as_view()),
    
]