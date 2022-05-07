from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from rest_framework import generics

from .forms import *
from .models import *
from .serializers import PointSerializer

menu = [{'title': "Войти", 'url_name': "login"},
        {'title': "Грамматика", 'url_name': "grammar"}
        ]


class PointList(ListView):
    model = Point
    template_name = 'catalog/index.html'
    context_object_name = 'points'
    extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

#def index(request):
#    points = Point.objects.all()

 #   context = {
 #       'points': points,
 #       'title': 'Главная страница',
  #      'category_selected': 0,
  #  }
  #  return render(request, 'catalog/index.html', context=context)


def grammar(request):
    return render(request, 'catalog/grammar.html', {'menu': menu, 'title': 'Грамматика'})


def addpoint(request):
    if request.method == 'POST':
        form = AddPointForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPointForm()
    return render(request, 'catalog/addpoint.html', {'form': form, 'menu': menu, 'title': 'Добавить пойнт'})


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def study_point(request, point_slug):
    point = get_object_or_404(Point, slug=point_slug)
    context = {
        'point': point,
        'title': point.title,
        'category_selected': point.category_id
    }

    return render(request, 'catalog/point.html', context=context)


def show_category(request, category_id):
    point = Point.objects.filter(category_id=category_id)

    if len(point) == 0:
        raise Http404()

    context = {
        'point': point,
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
