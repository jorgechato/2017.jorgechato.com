from django.conf.urls import url

from events.views import MainView

app_name = 'events'

urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),
]
