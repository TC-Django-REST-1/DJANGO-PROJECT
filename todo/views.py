from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import TodoOwner
from .models import Todo as TodoModel
from .serializers import TodoSerializer


class TodoBase:
    authentication_classes = [
        JWTAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = TodoSerializer
    model = TodoModel


class TodosView(TodoBase, ListAPIView, CreateAPIView):
    def get_queryset(self):
        queryset = self.model.objects.filter(author__pk=self.request.user.pk)
        return queryset.order_by("-created_at")


class TodoView(TodoBase, UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    permission_classes = [IsAuthenticated, TodoOwner]
    queryset = TodoModel.objects.all()
