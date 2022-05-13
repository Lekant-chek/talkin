from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL.")
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['id']

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Point(models.Model):
    title = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")
    text = models.TextField()
    translate = models.TextField()
    image = models.ImageField(upload_to='cards/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категории")
    tags = models.ManyToManyField(Tag, related_name='point', blank=True)
    student = models.ForeignKey(User, related_name='targets', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('point', kwargs={'point_slug': self.slug})

    class Meta:
        ordering = ['category']
        verbose_name = 'Учебные элементы'
        verbose_name_plural = 'Учебные элементы'

