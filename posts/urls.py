from django.urls import path
from rest_framework import routers
# from .views import PostList, PostDetail, UserList, UserDetail
from .views import UserViewSet, PostViewSet

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls