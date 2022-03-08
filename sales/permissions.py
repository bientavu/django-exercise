from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow only the object creator to PUT/DEL his/her object
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
