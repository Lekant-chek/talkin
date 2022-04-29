from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


@admin.register(models.Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'category', 'id']


@admin.register(models.Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ['student', 'point', 'create_at', 'is_complete']


admin.site.register(models.Level)
admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
