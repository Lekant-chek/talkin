"""chief URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from catalog.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'point', PointViewSet, basename='point')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('api/v1/', include(router.urls)),

    # path('api/v1/pointlist/', PointViewSet.as_view({'get': 'list'})),
    # path('api/v1/pointlist/<int:pk>/', PointViewSet.as_view({'put': 'update'})),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)