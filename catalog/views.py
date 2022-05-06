from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from rest_framework import generics
from .models import *
from .serializers import PointSerializer

menu = [{'title': "Войти", 'url_name': "login"},
        {'title': "Грамматика", 'url_name': "grammar"}
        ]


def index(request):
    points = Point.objects.all()

    context = {
        'points': points,
        'title': 'Главная страница',
        'category_selected': 0,
    }
    return render(request, 'catalog/index.html', context=context)


def grammar(request):
    return render(request, 'catalog/grammar.html', {'menu': menu, 'title': 'Грамматика'})


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def study_point(request, point_id):
    point = get_object_or_404(Point, pk=point_id)
    context = {
        'point': point,
        'title': point.title,
        'category_selected': point.category_id
    }

    return render(request, 'catalog/point.html', context=context)


def show_category(request, category_id):
    points = Point.objects.filter(category_id=category_id)

    if len(points) == 0:
        raise Http404()

    context = {
        'points': points,
        'title': 'Отображение по рубрикам',
        'category_id': category_id,

    }
    return render(request, 'catalog/index.html', context=context)


class PointAPIList(generics.ListCreateAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class HomeView(ListView):
    model = Point
    paginate_by = 5
    template_name = 'catalog/home.html'


class PointListView(ListView):
    model = Point

    def get_queryset(self):
        return Point.objects.filter(category__slug=self.kwargs.get('slug'))


class PointDetailView(DetailView):
    model = Point
    context_object_name = 'point'
    slug_url_kwarg = 'point_slug'
