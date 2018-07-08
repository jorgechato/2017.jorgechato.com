from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from ckeditor.widgets import CKEditorWidget
from django.utils.safestring import mark_safe

from work.models import Profile, Project, Experience, Technical


class ProfileAdmin(ImportExportActionModelAdmin):
    list_display = ('cover_image', 'get_full_name')
    list_display_links = ('cover_image',)

    def cover_image(self, obj):
        tag = '<img src="%s" width="100px">' % obj.avatar.url
        return mark_safe(tag)

    def bio_tags(self, obj):
        return obj.bio

    bio_tags.allow_tags = True


class ProjectsAdmin(ImportExportActionModelAdmin):
    list_display = ('cover_image', 'get_full_name',)
    list_display_links = ('cover_image', 'get_full_name')
    list_filter = ('owner_name', 'repo_name')
    search_fields = ('owner_name', 'repo_name')
    ordering = ('-updated_at',)

    def cover_image(self, obj):
        tag = '<img src="%s" width="100px">' % obj.thumbnail
        return mark_safe(tag)


class ExperienceAdmin(ImportExportActionModelAdmin):
    list_display = ('cover_image', 'company_name', 'start_at')
    list_display_links = ('cover_image', 'company_name')

    def cover_image(self, obj):
        tag = '<img src="%s" width="100px">' % obj.thumbnail
        return mark_safe(tag)


class TechnicalAdmin(ImportExportActionModelAdmin):
    list_display = ('category', 'skills',)
    list_display_links = ('category',)
    list_filter = ('category',)
    search_fields = ('skills',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectsAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Technical, TechnicalAdmin)
