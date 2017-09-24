
from django.db import models
from django.utils import timezone
# Create your models here.

class Contacts(models.Model):

    name = models.CharField(max_length=100)
    contact_number = models.PositiveIntegerField()
    email = models.EmailField()
    business = models.CharField(max_length=256, blank=True)
    date = models.DateTimeField(default=timezone.now)

    enquiry = models.TextField()

    def __str__(self):
        return self.name
    