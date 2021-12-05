# From blog import views
from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('blog.html', views.PostList.as_view(), name='blog'),
]
