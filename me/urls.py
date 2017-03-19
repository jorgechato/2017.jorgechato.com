from django.conf.urls import url

from me.views import MainView

app_name = 'me'

urlpatterns = [
        url(r'^$', MainView.as_view(), name='main'),
        ]
