from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet,
                    UserViewSet)

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups',
                GroupViewSet,
                basename='groups'
                )
router.register('users', UserViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comment'
                )
router.register('follow',
                FollowViewSet,
                basename='follow'
                )

urlpatterns = [
    path('v1/', include(router.urls)),
    # Базовые эндпоинты Djoser, для управления пользователями в Django:
    path('v1/', include('djoser.urls')),
    # JWT- эндпоинты, для управления JWT-токенами:
    path('v1/', include('djoser.urls.jwt')),
]
