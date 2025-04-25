from rest_framework import serializers
from .models import NavigationItem, CategoryItem, CategoryList


class NavigationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationItem
        fields = ["id", "title", "path", "icon", "order"]  # 序列化字段


class CategoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryItem
        fields = ["id", "name", "order", "resolution", "tags"]  # 序列化字段


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryList
        fields = ["id", "title", "order"]  # 序列化字段
