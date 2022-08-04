from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from .models import Todo as TodoModel


class TodoOwner(BasePermission):
    """
    Allows access only to Todo owners.
    """

    def has_permission(self, request: Request, view) -> bool:
        pk = request._request.path.split("/")[-2]
        user_pk = request.user.pk
        return TodoModel.objects.filter(pk=pk, author__pk=user_pk).exists()
