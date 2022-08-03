from django.urls import path
from .views import PostList, PostDetail

urlpattern = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view())
]