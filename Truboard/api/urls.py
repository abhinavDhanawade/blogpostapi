from django.urls import path
from .views import PostListView

urlpatterns = [
    path('posts/<slug:page>', PostListView.as_view(), name='post-list'),
]
