import os
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from chato.utilities import content_name


class Section(models.Model):
    thumbnail = ProcessedImageField(
        upload_to=content_name(os.path.join('landing', 'sections')),
        options={'quality': 60},
        blank=True,
    )
    title = models.CharField(max_length=240, blank=True)
    order = models.IntegerField()
    description = RichTextUploadingField()
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-order',)
