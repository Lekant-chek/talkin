"""chief URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from catalog.views import PointAPIList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),

    # path('api/v1/pointlist/', PointAPIList.as_view()),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)