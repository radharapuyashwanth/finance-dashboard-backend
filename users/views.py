from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User
from .permissions import IsAdminUserRole
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUserRole]
