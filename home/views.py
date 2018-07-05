from django.views.generic import TemplateView
from chato.settings import instagram_api, instagram_id

from home.models import Section


class MainView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MainView, self).get_context_data(*args, **kwargs)
        #  recent_media, next_ = instagram_api.user_recent_media(
        #  count=21,
        #  user_id='204441623',
        #  )
        #  print(recent_media)
        #  context['pictures'] = recent_media
        context['sections'] = Section.objects.filter(public=True)

        return context
