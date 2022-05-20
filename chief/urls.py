"""chief URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from catalog.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/talkin-auth/', include('rest_framework.urls')),
    path('', include('catalog.urls')),
    path('api/v1/point/', PointApiList.as_view()),
    path('api/v1/point/<int:pk>/', PointApiUpdate.as_view()),
    path('api/v1/pointdelete/<int:pk>/', PointApiDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)