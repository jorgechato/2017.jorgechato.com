from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic import ListView

from posts.models import Article


class ArticleDetailView(DetailView):
    model = Article


class ArticleListView(ListView):
    model = Article
    paginate_by = 5

    def get_queryset(self):
        queryset = super(ArticleListView, self).get_queryset()
        queryset = queryset.filter(
            public=True,
            published_at__lte=timezone.now()
        )
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(
            ArticleListView,
            self
        ).get_context_data(*args, **kwargs)
        return context
