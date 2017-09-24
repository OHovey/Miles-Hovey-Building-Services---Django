from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse





# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(blank=True, null=True)

    content = models.TextField()
    

    def __str__(self):
        return self.title

    def publish(self):
        self.published = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk}) 

    def get_queryset(self):
        return Post.objects.all()

