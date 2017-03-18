from django import forms
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from ckeditor.widgets import CKEditorWidget

from posts.models import Post


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = "__all__"


class PostAdmin(ImportExportActionModelAdmin):
    form = PostAdminForm

    list_display = ('cover_image', 'title', 'published_at', 'public', 'slug')
    list_filter = ('published_at', 'public')
    list_display_links = ('cover_image', 'title',)
    search_fields = ('title',)
    ordering = ('-published_at',)

    def cover_image(self, obj):
        tag = '<img src="https://placeholdit.imgix.net/~text?txtsize=23&bg=000000&txtclr=D3367E&txt=%s&w=200&h=100">' % obj.title
        if obj.thumbnail:
            tag = '<img src="https://placeholdit.imgix.net/~text?txtsize=23&bg=D3367E&txtclr=000000&txt=%s&w=200&h=100">' % obj.title
        return tag

    cover_image.allow_tags = True


admin.site.register(Post, PostAdmin)
