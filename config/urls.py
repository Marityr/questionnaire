from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quizes.urls', namespace='quizes')),
    path('', include('userdata.urls', namespace='userdata')),
    path('parsertable/', include('parsertable.urls', namespace='parsertable')),
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)