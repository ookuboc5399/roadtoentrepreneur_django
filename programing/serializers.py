from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Video



class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ['id','title','video','thum']