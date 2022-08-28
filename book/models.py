from django.db import models


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    author = models.CharField(max_length=40)
    quantityPages = models.CharField(max_length=4)
    yearLaunch = models.CharField(max_length=4)
