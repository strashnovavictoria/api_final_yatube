from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

app_name = 'api'
router = DefaultRouter()
router.register('v1/posts', PostViewSet, basename='v1/posts')
router.register('v1/groups', GroupViewSet, basename='v1/groups')
router.register(r'v1/posts/(?P<post_id>[^/.]+)/comments', CommentViewSet,
                basename='v1/comments')
router.register('v1/follow', FollowViewSet, basename='v1/follow')


urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
