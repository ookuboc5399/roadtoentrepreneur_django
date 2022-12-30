from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'created_at')
