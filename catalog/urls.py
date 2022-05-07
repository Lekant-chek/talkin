from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('<slug:slug>/<slug:point_slug>/', views.PointDetailView.as_view(), name='point_single'),
    # path('<slug:slug>/', views.PointListView.as_view(), name='point_list'),

    # path('', views.HomeView.as_view(), name='home'),
    path('', PointList.as_view(), name='home'),
    path('grammar/', grammar, name='grammar'),
    path('login/', login, name='login'),
    path('point/<slug:point_slug>/', study_point, name='point'),
    path('category/<int:category_id>/', show_category, name='category'),
    path('addpoint/', addpoint, name='addpoint'),
]