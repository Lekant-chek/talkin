from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

from . import models


@admin.register(models.Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ['student', 'title', 'get_html_image', 'category', 'text', 'translate', 'created_at']
    list_display_links = ('student', 'title')
    search_fields = ('category', 'text')
    list_editable = ('text', 'translate')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_image.short_description = "Изображение"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)

admin.site.site_header = 'Управление сайтом'
