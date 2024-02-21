from django.db import models

# Create your models here.

class Uploadfile(models.Model):
    file = models.FileField(upload_to='uploadfile/')
