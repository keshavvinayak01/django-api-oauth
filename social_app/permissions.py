from rest_framework import permissions

class isOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user 

class isSuperUserOrReadOnly(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user.is_superuser == True