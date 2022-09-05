from rest_framework import viewsets
from vacancy.api import serializers
from vacancy import models
from rest_framework.permissions import IsAuthenticated

class VacancyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    
    serializer_class = serializers.VacancySerializer
    queryset = models.Vacancy.objects.all()