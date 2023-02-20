from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    phone = models.IntegerField(null=True)
    date = models.DateField(null=True)