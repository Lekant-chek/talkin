from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


@admin.register(models.Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ['student', 'title', 'category', 'text', 'translate', 'created_at']
    list_display_links = ('student', 'title')
    search_fields = ('category', 'text')
    list_editable = ('text', 'translate')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
