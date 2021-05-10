from django.urls import path
from . import views
import django.contrib.auth.views as auth_views
from .views import Home, Postdetailview, Postcreateview, Postupdateview, PostDeleleteView, UserPostListView
urlpatterns = [
    path('', Home.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-post"),
    path("post/<int:pk>", Postdetailview.as_view(), name="post-detail"),
    path("post/update/<int:pk>", Postupdateview.as_view(), name="post-update"),
    path("post/delete/<int:pk>", PostDeleleteView.as_view(), name="post-delete"),
    path("create/", Postcreateview.as_view(), name="post-create"),

    path('about', views.about, name="blog-about")
]
