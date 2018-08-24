import os
from django.views.generic import TemplateView

from home.models import Section


class MainView(TemplateView):
    template_name = "home.html"

    def __init__(self, *args, **kwargs):
        super(MainView, self).__init__()
        self.access_token = os.environ.get('access_token')
        self.client_secret = os.environ.get('client_secret')
        self.instagram_id = os.environ.get('instagram_id')

    def get_context_data(self, *args, **kwargs):
        context = super(MainView, self).get_context_data(*args, **kwargs)
        #  recent_media, next_ = instagram_api.user_recent_media(
        #  count=21,
        #  user_id='204441623',
        #  )
        #  print(recent_media)
        #  context['pictures'] = recent_media
        context['sections'] = Section.objects.filter(public=True)
        context['amazon'] = ["test", "test"]

        return context
