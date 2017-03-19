from django.views.generic import TemplateView
from chato.settings import instagram_api

# from me.models import Event


class MainView(TemplateView):
    template_name = "me.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MainView, self).get_context_data(*args, **kwargs)
        recent_media, _next = instagram_api.user_recent_media()
        context['pictures'] = recent_media
        # context['events'] = Event.objects.all()

        return context
