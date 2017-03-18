from django import forms
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from ckeditor.widgets import CKEditorWidget

from profiles.models import Profile, Projects, Experience, Technical


class ProfileAdminForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileAdmin(ImportExportActionModelAdmin):
    form = ProfileAdminForm

    list_display = ('cover_image', 'get_full_name', 'bio_tags')
    list_display_links = ('cover_image',)

    def cover_image(self, obj):
        tag = '<img src="%s" width="100px">' % obj.avatar.url
        return tag

    def bio_tags(self, obj):
        return obj.bio

    cover_image.allow_tags = True
    bio_tags.allow_tags = True


class ProjectsAdmin(ImportExportActionModelAdmin):
    list_display = ('cover_image', 'get_full_name',)
    list_display_links = ('cover_image', 'get_full_name')
    list_filter = ('owner_name', 'repo_name')
    search_fields = ('owner_name', 'repo_name')
    ordering = ('-updated_at',)

    def cover_image(self, obj):
        tag = '<img src="%s" width="100px">' % obj.thumbnail.url
        return tag

    cover_image.allow_tags = True


class ExperienceAdmin(ImportExportActionModelAdmin):
    list_display = ('cover_image', 'company_name', 'start_at')
    list_display_links = ('cover_image', 'company_name')

    def cover_image(self, obj):
        tag = '<img src="%s" width="100px">' % obj.thumbnail.url
        return tag

    cover_image.allow_tags = True


class TechnicalAdmin(ImportExportActionModelAdmin):
    list_display = ('category', 'skills',)
    list_display_links = ('category',)
    list_filter = ('category',)
    search_fields = ('skills',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Technical, TechnicalAdmin)
