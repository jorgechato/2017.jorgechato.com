from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from slugify import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from chato.utilities import UploadPath


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=240)
    slug = models.SlugField(max_length=240, blank=True, editable=False)
    content = RichTextUploadingField()
    published_at = models.DateTimeField()
    public = models.BooleanField(default=True)
    thumbnail = ProcessedImageField(
        upload_to=UploadPath('articles'),
        options={'quality': 60},
        blank=True,
    )

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.slug

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*arg, **kwargs)

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'slug': self.slug})

    class Meta:
        unique_together = ('title',)
        ordering = ('-published_at',)
