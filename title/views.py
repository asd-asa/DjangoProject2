from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NavigationItem, CategoryItem, CategoryList
from .serializers import (
    NavigationItemSerializer,
    CategoryItemSerializer,
    CategoryListSerializer,
)


class NavigationBarView(APIView):
    """
    壁纸首页头部导航栏接口视图
    """

    def get(self, request):
        navigation_items = NavigationItem.objects.all()  # 获取所有导航项
        serializer = NavigationItemSerializer(navigation_items, many=True)
        return Response(serializer.data)  # 返回序列化后的数据


class CategoryItemView(APIView):
    """
    分类列表接口视图
    """

    def get(self, request):
        category_items = CategoryItem.objects.all()  # 获取所有分类项
        serializer = CategoryItemSerializer(category_items, many=True)
        return Response(serializer.data)  # 返回序列化后的数据


class CategoryListView(APIView):
    """
    分类列表接口视图
    """

    def get(self, request):
        category_items = CategoryList.objects.all()  # 获取所有分类项
        serializer = CategoryListSerializer(category_items, many=True)
        return Response(serializer.data)  # 返回序列化后的数据
