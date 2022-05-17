from rest_framework import serializers
from .models import Point


class PointSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    slug = serializers.CharField(max_length=255)
    text = serializers.CharField()
    translate = serializers.CharField()
    category_id = serializers.IntegerField()
    student_id = serializers.IntegerField()
    created_at = serializers.DateField(read_only=True)
    is_complete = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Point.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.text = validated_data.get('text', instance.text)
        instance.translate = validated_data.get('translate', instance.translate)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.student_id = validated_data.get('student_id', instance.student_id)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.is_complete = validated_data.get('is_complete', instance.is_complete)
        instance.save()
        return instance

