from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *
from .serializers import PointSerializer


class PointList(DataMixin, ListView):
    model = Point
    template_name = 'catalog/index.html'
    context_object_name = 'points'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Point.objects.filter(is_complete=False)


class Categories(DataMixin, ListView):
    model = Point
    template_name = 'catalog/index.html'
    context_object_name = 'points'
    allow_empty = False

    def get_queryset(self):
        return Point.objects.filter(category__slug=self.kwargs['category_slug'], is_complete=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['points'][0].category),
                                      category_selected=context['points'][0].category_id)
        return dict(list(context.items()) + list(c_def.items()))


class AddPoint(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPointForm
    template_name = 'catalog/addpoint.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление учебного материала')
        return dict(list(context.items()) + list(c_def.items()))


class StudyPoint(DataMixin, DetailView):
    model = Point
    template_name = 'catalog/point.html'
    slug_url_kwarg = 'point_slug'
    context_object_name = 'point'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['point'])
        return dict(list(context.items()) + list(c_def.items()))


def grammar(request):
    return render(request, 'catalog/grammar.html', {'menu': menu, 'title': 'Грамматика'})


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


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


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'catalog/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'catalog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))