from django.urls import path
from .views import PostListView, postDetailView

urlpatterns = [
    path('', PostListView.as_view()),
    path('post/<slug:slug>/', postDetailView, name='post_detail')
]
