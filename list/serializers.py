from rest_framework import serializers
from django.db import models
from .models import List


class List(serializers.Serializer):
    id = models.AutoField(primary_key=True)
    contents = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    deleted_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = List
        fields = ('id', 'contents', 'created_at', 'updatedd_at', 'deleted_at')
