from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPointForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = ['title', 'slug', 'text', 'translate', 'image', 'category', 'student']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 20:
            raise ValidationError('Длина превышает 50 символов')

        return title
