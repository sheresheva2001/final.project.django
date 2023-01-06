from . import views
from django.urls import path
from .feeds import LatestPostsFeed
from django.contrib import admin




urlpatterns = [
    path('admin/', admin.site.urls),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]


