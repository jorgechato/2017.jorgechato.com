from django.conf.urls import url

from profiles.views import RepoDetailView, MainView

app_name = 'profile'

urlpatterns = [
        url(r'^repo/(?P<slug>[-\w]+)/$', RepoDetailView.as_view(), name='repo'),
        url(r'^$', MainView.as_view(), name='main'),
        ]
