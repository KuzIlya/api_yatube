from api.views import CommentViewSet, GroupViewSet, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')
