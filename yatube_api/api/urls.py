
from rest_framework import routers
from django.urls import path, include
from rest_framework.authtoken import views
from api.views import PostViewSet, GroupViewSet, CommentViewSet


v1_router = routers.DefaultRouter()

v1_router.register('posts', PostViewSet, basename='post')
v1_router.register('groups', GroupViewSet, basename='group')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')



urlpatterns = [
    path('', include(v1_router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('v1/', include('api.urls')),
]
