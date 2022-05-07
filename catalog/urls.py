from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('<slug:slug>/<slug:point_slug>/', views.PointDetailView.as_view(), name='point_single'),
    # path('<slug:slug>/', views.PointListView.as_view(), name='point_list'),

    # path('', views.HomeView.as_view(), name='home'),
    path('', PointList.as_view(), name='home'),
    path('addpoint/', AddPoint.as_view(), name='addpoint'),
    path('grammar/', grammar, name='grammar'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('point/<slug:point_slug>/', StudyPoint.as_view(), name='point'),
    path('category/<slug:category_slug>/', Categories.as_view(), name='category'),
]