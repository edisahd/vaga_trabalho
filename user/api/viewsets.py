from rest_framework import viewsets
from user.api import serializers
from user import models
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    
    serializer_class = serializers.UserSerializers
    queryset = models.User.objects.all()