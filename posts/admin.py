from django import forms
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from ckeditor.widgets import CKEditorWidget
from django.utils.safestring import mark_safe

from posts.models import Article


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = "__all__"


class ArticleAdmin(ImportExportActionModelAdmin):
    form = ArticleAdminForm

    list_display = ('cover_image', 'title', 'published_at', 'public', 'slug')
    list_filter = ('published_at', 'public')
    list_display_links = ('cover_image', 'title',)
    search_fields = ('title',)
    ordering = ('-published_at',)

    def cover_image(self, obj):
        tag = '<img src="https://placeholdit.imgix.net/~text?txtsize=23&bg=000000&txtclr=FFFFFF&txt=%s&w=200&h=100">' % obj.title
        if obj.thumbnail:
            tag = '<img src="%s" width="100px">' % obj.thumbnail.url
        return mark_safe(tag)


admin.site.register(Article, ArticleAdmin)
