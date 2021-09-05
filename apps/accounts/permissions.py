from rest_framework import permissions


class IsMyUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # lectura permitida
        if request.method in permissions.SAFE_METHODS:
            return True

        # permiso de escrtura solo para el propietario del usuario
        return obj.id == request.user.id
