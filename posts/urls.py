from django.conf.urls import url

from posts.views import PostDetailView, PostListView

app_name = 'articles'

urlpatterns = [
        url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='detail'),
        url(r'^', PostListView.as_view(), name='list'),
        ]
