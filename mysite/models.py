from django.db import models


class Line(models.Model):
    text = models.CharField(max_length=255)


class Students(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()


class Person:
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)

    def __init__(self, name, age, sex, account_type, tags):
        self.name = name
        self.age = age
        self.sex = sex
        self.account_type = account_type
        self.tags = tags
