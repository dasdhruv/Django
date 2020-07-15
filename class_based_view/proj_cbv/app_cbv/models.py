from django.db import models
from django.conf import settings
# Create your models here.
# Every class is representing a db table
class School(models.Model):
    name = models.CharField(max_length = 25)
    principal = models.CharField(max_length = 20)
    location = models.CharField(max_length = 80)

    #REQUIRED_FIELDS = ['name']
    #USERNAME_FIELD = ['site']
    def __str__(this):
        return this.name

class Student(models.Model):
    name = models.CharField(max_length = 20)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name = 'student', on_delete = models.CASCADE)

    def __str__(this):
        return this.name
