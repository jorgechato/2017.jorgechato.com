from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from ckeditor.widgets import CKEditorWidget
from django.utils.safestring import mark_safe


from events.models import Event
from events.models import Description


class DescriptionAdmin(ImportExportActionModelAdmin):
    list_display = ('cover_image', 'title', 'created_at', 'public')
    list_display_links = ('cover_image',)
    list_filter = ('created_at', 'public')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

    def cover_image(self, obj):
        tag = '<img src="https://placeholdit.imgix.net/~text?txtsize=23&bg=000000&txtclr=D3367E&txt=%s&w=200&h=100">' % obj.title
        if obj.thumbnail:
            tag = '<img src="%s" width="100px">' % obj.thumbnail.url
        return mark_safe(tag)


class EventAdmin(ImportExportActionModelAdmin):
    list_display = ('cover_image', 'title', 'description_tags')
    list_display_links = ('cover_image',)
    search_fields = ('title', 'description')
    ordering = ('-start_at',)

    def cover_image(self, obj):
        tag = '<img src="%s" width="100px">' % obj.thumbnail.url
        return mark_safe(tag)

    def description_tags(self, obj):
        return obj.description

    description_tags.allow_tags = True


admin.site.register(Event, EventAdmin)
admin.site.register(Description, DescriptionAdmin)
