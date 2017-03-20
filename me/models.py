from django.db import models
from ckeditor.fields import RichTextField


class Event(models.Model):
    thumbnail = models.ImageField(upload_to="events/")
    title = models.CharField(max_length=240)
    url = models.URLField(blank=True)
    location = models.CharField(max_length=240, blank=True)
    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    description = RichTextField()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-start_at',)
