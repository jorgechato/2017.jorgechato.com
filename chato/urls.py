from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    url(r'^articles/', include('posts.urls'), name="articles"),
    url(r'^events/', include('events.urls'), name="events"),
    url(r'^work/', include('work.urls'), name="work"),
    url(r'^admin/', admin.site.urls),
    url(r'^editor/', include('ckeditor_uploader.urls')),
    url(r'^', include('home.urls'), name="home"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
