from rest_framework import permissions

class has_permission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'PATCH':
            if request.user.is_superuser:
                return True
            else:
                return False
        elif request.method == 'POST':
            return True

        return True
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
                return True
        return False    