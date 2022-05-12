from django.db.models import Count

from .models import *

menu = [{'title': "Грамматика", 'url_name': "grammar"},
        {'title': "Добавить учебные материалы", 'url_name': "addpoint"}
        ]


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        category = Category.objects.annotate(Count('point'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu
        context['category'] = category
        if 'category_selected' not in context:
            context['category_selected'] = 0
        return context
