from attr import field
from rest_framework import serializers
from user import models

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'