from rest_framework.permissions import BasePermission, SAFE_METHODS


class RecordAccessPermission(BasePermission):
    """
    Viewer: read only
    Analyst: read only (records + summary)
    Admin: full CRUD
    """

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        if request.method in SAFE_METHODS:
            return user.role in ['viewer', 'analyst', 'admin']

        return user.role == 'admin'
