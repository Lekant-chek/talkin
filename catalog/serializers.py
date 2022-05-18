from rest_framework import serializers
from .models import Point


class PointSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Point
        fields = ('title', 'text', 'slug', 'translate', 'category', 'student')

