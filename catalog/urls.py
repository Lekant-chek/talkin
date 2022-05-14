from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', PointList.as_view(), name='home'),
    path('addpoint/', AddPoint.as_view(), name='addpoint'),
    path('grammar/', grammar, name='grammar'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('point/<slug:point_slug>/', StudyPoint.as_view(), name='point'),
    path('category/<slug:category_slug>/', Categories.as_view(), name='category'),
]