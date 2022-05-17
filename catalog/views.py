from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView

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
        return Point.objects.filter(is_complete=False).select_related('category')


class Categories(DataMixin, ListView):
    model = Point
    template_name = 'catalog/index.html'
    context_object_name = 'points'
    allow_empty = False

    def get_queryset(self):
        return Point.objects.filter(category__slug=self.kwargs['category_slug'], is_complete=False).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      category_selected=c.pk)
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


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'catalog/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'catalog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def grammar(request):
    return render(request, 'catalog/grammar.html', {'menu': menu, 'title': 'Грамматика'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class PointAPIView(APIView):
    def get(self, request):
        p = Point.objects.all()
        return Response({'points': PointSerializer(p, many=True).data})

    def post(self, request):
        serializer = PointSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'point': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Point.objects.get(pk=pk)

        except:
            return Response({'error': 'Object PUT not allowed'})

        serializer = PointSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


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

