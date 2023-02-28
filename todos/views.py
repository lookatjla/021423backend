from .models import Todo
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TodoSerializer

# This file creates all routes


class TodoViewSet(viewsets.ModelViewSet):
    # The Main Query for the index route
    queryset = Todo.objects.all()
    # The serializer class for serializing output
    serializer_class = TodoSerializer
    # optional permission class set permission level
    # Coule be [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
