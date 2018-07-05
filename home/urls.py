from django.conf.urls import url

from home.views import MainView

app_name = 'home'

urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),
]
