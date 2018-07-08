from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Section(models.Model):
    thumbnail = models.ImageField(upload_to='sections', blank=True)
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
