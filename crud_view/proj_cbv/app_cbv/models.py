from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.
# Every class is representing a db table
class School(models.Model):
    name = models.CharField(max_length = 25)
    principal = models.CharField(max_length = 20)
    location = models.CharField(max_length = 80)

    def __str__(this):
        return this.name

    """
        get_absolute_url is defined as after inserting new records into school table would be able to redirect the control to some page
    """
    def get_absolute_url(this):
        return reverse('app_cbv:school_details', kwargs = {'pk':this.pk})

class Student(models.Model):
    name = models.CharField(max_length = 20)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name = 'student', on_delete = models.CASCADE)

    def __str__(this):
        return this.name
