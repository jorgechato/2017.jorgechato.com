from django.views.generic import TemplateView, DetailView

from profiles.models import Experience, Profile, Projects, Technical


class RepoDetailView(DetailView):
    model = Projects


class MainView(TemplateView):
    template_name = "work.html"
