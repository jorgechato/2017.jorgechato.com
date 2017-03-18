from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic import ListView

from posts.models import Post


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        queryset = queryset.filter(public=True,
                                   published_at__lte=timezone.now())
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        return context
