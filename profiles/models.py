from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
import chato.settings as ls


class Profile(models.Model):
    first_name = models.CharField(max_length=240, blank=True, editable=False)
    last_name = models.CharField(max_length=240, blank=True, editable=False)
    email = models.EmailField(blank=True, editable=False)
    bio = RichTextField()
    avatar = models.URLField()
    cv = models.URLField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def save(self, *arg, **kwargs):
        user = User.objects.get(email=ls.email)
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.email = user.email
        super(Profile, self).save(*arg, **kwargs)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class Technical(models.Model):
    category = models.CharField(max_length=240)
    skills = models.TextField()

    def __str__(self):
        return self.category

    def __unicode__(self):
        return self.category


class Experience(models.Model):
    thumbnail = models.URLField()
    company_name = models.CharField(max_length=240)
    position = models.CharField(max_length=240, blank=True)
    url = models.URLField(blank=True)
    location = models.CharField(max_length=240, blank=True)
    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    description = RichTextField()

    def __str__(self):
        return self.company_name

    def __unicode__(self):
        return self.company_name

    class Meta:
        ordering = ('-start_at',)


class Project(models.Model):
    thumbnail = models.URLField()
    owner_name = models.CharField(max_length=240)
    repo_name = models.CharField(max_length=240)
    description = models.TextField(blank=True, editable=False)
    url = models.URLField(blank=True, editable=False)
    updated_at = models.DateTimeField(blank=True, editable=False)
    slug = models.SlugField(max_length=240, blank=True, editable=False)

    def __str__(self):
        return self.repo_name

    def __unicode__(self):
        return self.repo_name

    def save(self, *arg, **kwargs):
        self.slug = "{}-{}".format(self.owner_name, self.repo_name)
        repo = ls.github_api.get_repo(
                "{}/{}".format(self.owner_name, self.repo_name))
        self.description = repo.description
        self.url = repo.html_url
        self.updated_at = repo.updated_at
        super(Project, self).save(*arg, **kwargs)

    def get_full_name(self):
        return "{}/{}".format(self.owner_name, self.repo_name)

    def get_absolute_url(self):
        return reverse('profile:repo', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('-updated_at',)
