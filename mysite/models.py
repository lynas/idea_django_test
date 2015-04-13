from django.db import models


class Line(models.Model):
    text = models.CharField(max_length=255)


class Students(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()
