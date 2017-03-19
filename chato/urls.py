from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    url(r'^articles/', include('posts.urls'), name="articles"),
    url(r'^me/', include('me.urls'), name="me"),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('profiles.urls'), name="profile"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
