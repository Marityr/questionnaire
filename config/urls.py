from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quizes.urls', namespace='quizes')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
