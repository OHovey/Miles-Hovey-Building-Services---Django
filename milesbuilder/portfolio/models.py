from django.db import models


# Create your models here.

class Project(models.Model):

    overview = models.CharField(max_length=100)
    description_of_work = models.TextField()
    

    def __str__(self):
        return self.overview

class Image(models.Model):

    picture = models.FileField(null=True, blank=True)
    project = models.ForeignKey(Project, related_name='images')

    def __str__(self):
        return self.picture.url



