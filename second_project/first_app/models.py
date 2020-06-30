from django.db import models
# Create your models here.
# The Topic will be converted into a rdbms table
class Topic(models.Model):
    top_name = models.CharField(max_length = 256, unique = True)
    def __str__(this):
        return this.top_name

class Webpage(models.Model):
    # topic will be foreign key of top_name
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    name = models.CharField(max_length = 245, unique =  True)
    url = models.URLField(unique = True)

    def __str__(this):
        return this.name

class AccessRecord(models.Model):
    name_webpage = models.ForeignKey(Webpage, on_delete = models.CASCADE)
    date = models.DateField()

    def __str__(this):
        this.date = str(this.date)
        return this.date
