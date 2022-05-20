# Generated by Django 4.0.4 on 2022-05-18 01:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0003_alter_point_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
