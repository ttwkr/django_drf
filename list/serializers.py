from rest_framework import serializers
from django.db import models
from .models import *
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
        fields = (
            "id",
            "contents",
            "image_list",
            "created_at",
            "updated_at",
            "deleted_at",
        )

    def get_image_list(self, obj):
        return json.loads(obj.image_list)


class BestSerializer(serializers.ModelSerializer):
    todo = TodolistSerializer()

    class Meta:
        model = Bests
        fields = "__all__"


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class ShopDetailSerializer(serializers.ModelSerializer):
    item = ItemSerializer(required=False, many=True)

    class Meta:
        model = Shop
        fields = ["id", "name", "item"]


class MapShopListSerializer(serializers.Serializer):
    class Meta:
        model = Shop
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    shop = ShopSerializer()

    class Meta:
        model = Likes
        fields = "__all__"
