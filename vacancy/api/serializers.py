from rest_framework import serializers
from vacancy import models

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = '__all__'