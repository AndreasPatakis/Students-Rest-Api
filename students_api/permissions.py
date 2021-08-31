from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile ONLY"""

    def has_object_permission(self, request, view, obj):
        """Check if the request is a SAFE METHOD(like get where nothing gets edited)"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnNotes(permissions.BasePermission):
    """Allow user to edit their own notes ONLY"""

    def has_object_permission(self, request, view, obj):
        """Check if the request is a SAFE METHOD(like get where nothing gets edited)"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_student == request.user
