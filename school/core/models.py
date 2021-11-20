from django.core.exceptions import ValidationError
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    grade = models.FloatField(null=True)


    def __str__(self):
        return self.name

