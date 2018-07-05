from django.views.generic import TemplateView

from events.models import Event, Description


class MainView(TemplateView):
    template_name = "events.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MainView, self).get_context_data(*args, **kwargs)
        context['descriptions'] = Description.objects.filter(public=True)
        context['events'] = Event.objects.all()

        return context
