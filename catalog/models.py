import uuid

from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Level(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Point(models.Model):
    name = models.CharField(max_length=100, blank=True)
    text = models.TextField()
    translate = models.TextField()
    image = models.ImageField(upload_to='cards/', blank=True)
    category = models.ForeignKey(
        Category,
        related_name='point',
        on_delete=models.SET_NULL,
        null=True
    )
    level = models.ForeignKey(
        Level,
        related_name='point',
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, related_name='point', blank=True)

    class Meta:
        ordering = ['level']

    def __str__(self):
        return self.name


class Target(models.Model):
    student = models.ForeignKey(User, related_name='targets', on_delete=models.CASCADE)
    point = models.ForeignKey(Point, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return f"self.create_at"
