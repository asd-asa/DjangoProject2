from rest_framework import serializers
from .models import Wallpaper
from rest_framework.pagination import PageNumberPagination


class WallpaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallpaper
        fields = "__all__"


class WallpaperPagination(PageNumberPagination):
    page_size = 9  # 每页显示的图片数量
    page_size_query_param = "page_size"  # 允许客户端通过查询参数指定每页数量
    max_page_size = 100  # 每页最大数量限制
