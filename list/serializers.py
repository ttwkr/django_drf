from rest_framework import serializers
from django.db import models
from .models import TodoList
import json


class TodolistSerializer(serializers.ModelSerializer):
    id = models.AutoField(primary_key=True)
    contents = serializers.CharField(required=False)
    image_list = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    deleted_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = TodoList
        fields = ('id', 'contents', 'image_list',
                  'created_at', 'updated_at', 'deleted_at',)

    def get_image_list(self, obj):
        return json.loads(obj.image_list)
