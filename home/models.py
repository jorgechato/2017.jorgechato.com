from django.db import models
from slugify import slugify
from ckeditor.fields import RichTextField


class Section(models.Model):
    thumbnail = models.ImageField(upload_to='sections', blank=True)
    title = models.CharField(max_length=240, blank=True)
    order = models.IntegerField()
    description = RichTextField()
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-order',)
