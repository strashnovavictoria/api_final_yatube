from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'
router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register('posts/(?P<post_id>[^/.]+)/comments', CommentViewSet,
                basename='comments'),
router.register(r'follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
