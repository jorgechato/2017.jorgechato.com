from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from ckeditor.widgets import CKEditorWidget
from django.utils.safestring import mark_safe


from home.models import Section


class SectionAdmin(ImportExportActionModelAdmin):
    list_display = ('cover_image', 'order', 'title', 'public')
    list_display_links = ('cover_image',)
    search_fields = ('title', 'order')
    ordering = ('-order',)

    def cover_image(self, obj):
        tag = '<img src="https://placeholdit.imgix.net/~text?txtsize=23&bg=000000&txtclr=FFFFFF&txt=%s&w=200&h=100">' % obj.title
        if obj.thumbnail:
            tag = '<img src="%s" width="100px">' % obj.thumbnail.url
        return mark_safe(tag)


admin.site.register(Section, SectionAdmin)
