from rest_framework import permissions


class PostAuthPermission(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS
                or obj.author == request.user):
            return True


class CommentAuthPermission(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
