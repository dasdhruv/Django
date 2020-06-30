from django.db import models
# Create your models here.
# The Topic will be converted into a rdbms table
class Users(models.Model):
    user_name = models.CharField(max_length = 256, unique = True)
    user_lastname = models.CharField(max_length = 25)
    user_email = models.EmailField(max_length=255, unique=True)
    def __str__(this):
        return this.user_name

    def __str__(this):
        return this.user_lastname

    def __str__(this):
        return this.user_email
