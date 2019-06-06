from rest_framework import (
    viewsets,
)
from rest_framework.permissions import IsAuthenticated

from api.v0.serializers.user import UserSerializer
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ['options', 'patch', 'put', 'get', 'post']
    resource_name = 'customers'
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
