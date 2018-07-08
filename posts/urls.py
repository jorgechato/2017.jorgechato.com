from django.conf.urls import url

from posts.views import ArticleDetailView, ArticleListView, ArticleSearchListView

app_name = 'articles'

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='detail'),
    url(r'^search', ArticleSearchListView.as_view(), name='search'),
    url(r'^', ArticleListView.as_view(), name='list'),
]
