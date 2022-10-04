from django.db import models

# Create your models here.
class Members(models.Model):
    firstname=models.CharField(max-size=255)