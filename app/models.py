from django.db import models

# Create your models here.

# Create your models here.
from django.db import models
from django.core.validators import *
# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=100,validators=[MinLengthValidator(5)])
    sid=models.IntegerField(primary_key=True)
    semail=models.EmailField()
    def __str__(self):
        return self.sname