import base64
import os
from django.views.generic import TemplateView, DetailView
from chato.settings import github_api
import markdown2
from chato.settings import MEDIA_ROOT

from profiles.models import Experience, Project, Technical


class RepoDetailView(DetailView):
    model = Project

    def get_context_data(self, *args, **kwargs):
        context = super(RepoDetailView, self).get_context_data(*args, **kwargs)
        repo_full_name = "{}/{}".format(
                self.object.owner_name,
                self.object.repo_name)

        repo = github_api.get_repo(repo_full_name)
        encod_readme = repo.get_readme().content

        readme = base64.b64decode(encod_readme)

        directory = MEDIA_ROOT
        if not os.path.exists(directory):
            os.makedirs(directory)

        f = open('{}/{}.md'.format(directory, self.object.repo_name), 'wb+')
        f.write(readme)
        f.close()

        test = markdown2.markdown_path(
                '{}/{}.md'.format(MEDIA_ROOT, self.object.repo_name),
                extras=[
                    "fenced-code-blocks",
                    "code-friendly",
                    "pyshell",
                    "pygments",
                    ])

        context['readme'] = test

        return context


class MainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MainView, self).get_context_data(*args, **kwargs)
        context['repos'] = Project.objects.all()
        context['skills'] = Technical.objects.all()
        context['experiences'] = Experience.objects.all()

        return context
