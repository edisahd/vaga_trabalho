from django.db import models

# Create your models here.

class Vacancy(models.Model):
    doc_id = models.CharField(primary_key=True, max_length=500)
    employer_name = models.CharField(max_length=500)
    date_posted = models.CharField(max_length=500)
    employment_type = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=50000)
    
    class Meta:
        db_table = 'TB_VACANCY'