from django import forms
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from ckeditor.widgets import CKEditorWidget

from me.models import Event


class EventAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Event
        fields = "__all__"


class EventAdmin(ImportExportActionModelAdmin):
    form = EventAdminForm

    list_display = ('cover_image', 'title', 'description_tags')
    list_display_links = ('cover_image',)
    search_fields = ('title', 'description')
    ordering = ('-start_at',)

    def cover_image(self, obj):
        tag = '<img src="%s" width="100px">' % obj.thumbnail
        return tag

    def description_tags(self, obj):
        return obj.description

    cover_image.allow_tags = True
    description_tags.allow_tags = True


admin.site.register(Event, EventAdmin)
