from __future__ import unicode_literals
import os

from django.db import models
from django.core.urlresolvers import reverse
from slugify import slugify
from ckeditor.fields import RichTextField
from django.utils import timezone


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    slug = slugify(instance.title)
    today = timezone.now().strftime('%Y-%b-%d')
    filename = "{}/{}/cover.{}".format(today, slug, ext)
    return os.path.join('historias/', filename)


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=240)
    slug = models.SlugField(max_length=240, blank=True, editable=False)
    content = RichTextField()
    published_at = models.DateTimeField()
    public = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to=content_file_name, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.slug

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*arg, **kwargs)

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'slug': self.slug})

    class Meta:
        unique_together = ('title',)
        ordering = ('-published_at',)
