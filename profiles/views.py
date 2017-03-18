import base64
from markdown2 import Markdown
from urllib.request import urlopen
from django.views.generic import TemplateView, DetailView
from chato.local_settings import github_api

from profiles.models import Experience, Profile, Projects, Technical


class RepoDetailView(DetailView):
    model = Projects

    def get_context_data(self, *args, **kwargs):
        context = super(RepoDetailView, self).get_context_data(*args, **kwargs)
        repo_full_name = "{}/{}".format(self.object.owner_name, self.object.repo_name)

        repo = github_api.get_repo(repo_full_name)
        encod_readme = repo.get_readme().content
        # readme_url = repo.get_readme().url
        # readme = urlopen(readme_url)

        markdowner = Markdown()
        readme = base64.b64decode(encod_readme)
        context['readme'] = markdowner.convert(readme)
        # context['readme'] = readme.read()

        return context


class MainView(TemplateView):
    template_name = "work.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MainView, self).get_context_data(*args, **kwargs)
        context['repos'] = Projects.objects.all()
        context['skills'] = Technical.objects.all()

        return context
