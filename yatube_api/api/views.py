from api.permissions import CommentAuthPermission, PostAuthPermission
from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer, UserSerializer)
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Comment, Follow, Group, Post, User
from rest_framework import permissions, viewsets, filters, pagination


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PostAuthPermission, )
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = [filters.SearchFilter, ]
    search_fields = ('following__username', )

    def get_queryset(self):
        new_queryset = self.request.user.follower.all()
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (CommentAuthPermission, )

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get("post_id"))

    def get_queryset(self):
        post = self.get_post()
        new_queryset = Comment.objects.filter(post=post)
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())
