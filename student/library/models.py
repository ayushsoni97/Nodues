from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(default=0)
    email = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Choice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    clear = models.CharField(max_length=10)

    def __str__(self):
        return self.clear
