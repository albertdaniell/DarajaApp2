from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    body = serializers.CharField(style={'base_template': 'textarea.html'})
    def create(self, validated_data):
        """
        Create and return a new `blog` instance, given the validated data.
        """
        return Blog.objects.create(**validated_data)
    def update(self, instance, validated_data):
        """
        Update and return an existing `blog` instance, given the validated data.

        """
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance
