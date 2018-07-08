from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
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


class ArticleSearchListView(ListView):
    model = Article
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ArticleSearchListView, self).get_queryset()
        queryset = queryset.filter(
            public=True,
            published_at__lte=timezone.now()
        )

        keywords = self.request.GET.get('q')
        if keywords:
            query = SearchQuery(keywords)
            title_vector = SearchVector('title', weight='A')
            content_vector = SearchVector('content', weight='B')
            vectors = title_vector + content_vector
            queryset = queryset.annotate(search=vectors).filter(search=query)
            queryset = queryset.annotate(
                rank=SearchRank(vectors, query)
            ).order_by('-rank')

        return queryset
