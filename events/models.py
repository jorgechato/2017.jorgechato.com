import os
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from chato.utilities import content_name


class Event(models.Model):
    thumbnail = ProcessedImageField(
        upload_to=content_name(os.path.join('events', 'events')),
        options={'quality': 60}
    )
    title = models.CharField(max_length=240)
    url = models.URLField(blank=True)
    location = models.CharField(max_length=240, blank=True)
    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    description = RichTextUploadingField()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-start_at',)


class Description(models.Model):
    title = models.CharField(max_length=240, blank=True)
    content = RichTextUploadingField()
    thumbnail = ProcessedImageField(
        upload_to=content_name(os.path.join('events', 'descriptions')),
        options={'quality': 60},
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)
