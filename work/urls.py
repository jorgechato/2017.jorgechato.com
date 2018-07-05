from django.conf.urls import url

from work.views import RepoDetailView, MainView

app_name = 'work'

urlpatterns = [
    url(r'^repo/(?P<slug>[-\w]+)/$', RepoDetailView.as_view(), name='repo'),
    url(r'^$', MainView.as_view(), name='main'),
]
