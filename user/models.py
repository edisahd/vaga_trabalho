from django.db import models
from uuid import uuid4

# Create your models here.

class User(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name_user = models.CharField(max_length=100)
    pass_user = models.CharField(max_length=100)
    email_user = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'TB_USER'