from PIL import Image
from rest_framework import generics, status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Wallpaper
from .serializers import WallpaperSerializer, WallpaperPagination


# 获取和创建壁纸的视图
class WallpaperListCreate(generics.ListCreateAPIView):
    queryset = Wallpaper.objects.all()
    serializer_class = WallpaperSerializer


# 获取、更新和删除单个壁纸的视图
class WallpaperDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wallpaper.objects.all()
    serializer_class = WallpaperSerializer


# 批量上传壁纸的视图
class BulkUploadView(APIView):
    parser_classes = (MultiPartParser,)  # 指定该视图使用 MultiPartParser 解析器，
    # 用于处理 multipart/form-data 类型的请求，通常用于文件上传

    # 这里可以添加认证和权限类
    # authentication_classes = []#（注释掉的代码）用于定义视图的认证方式。
    # 如果为空或未设置，则视图不强制进行用户认证，任何用户都可以访问
    # permission_classes = []

    def post(self, request):
        files = request.FILES.getlist("images")
        created_data = []

        for img in files:
            try:
                # 使用 Pillow 获取图片宽度和高度
                image = Image.open(img)
                width, height = image.size

                # 创建 Wallpaper 对象
                wallpaper = Wallpaper.objects.create(
                    title=request.POST.get(
                        "title", img.name.split(".")[0]
                    ),  # 从 POST 获取标题
                    image=img,
                    category=request.POST.get("category", "未分类"),  # 从 POST 获取分类
                    description=request.POST.get("description", ""),  # 从 POST 获取描述
                    tags=request.POST.get("tags", []),  # 从 POST 获取标签
                    resolution=f"{width}x{height}",  # 获取分辨率
                )
                created_data.append(WallpaperSerializer(wallpaper).data)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {"count": len(created_data), "results": created_data},
            status=status.HTTP_201_CREATED,
        )


# 壁纸列表分类视图
# class WallpaperListView(ListAPIView):
#     queryset = Wallpaper.objects.all()
#     serializer_class = WallpaperSerializer
#     pagination_class = WallpaperPagination  # 指定分页类
from rest_framework.generics import ListAPIView
from .models import Wallpaper
from .serializers import WallpaperSerializer, WallpaperPagination


class WallpaperListView(ListAPIView):
    """
    壁纸列表视图，支持分页功能。
    """

    queryset = Wallpaper.objects.all()  # 获取所有壁纸对象
    serializer_class = WallpaperSerializer  # 使用 WallpaperSerializer 进行序列化
    pagination_class = WallpaperPagination  # 指定分页类

    def get_queryset(self):
        """
        可重写此方法以动态调整查询集。
        """
        queryset = super().get_queryset()
        # 可根据请求参数进行过滤，例如按分类筛选
        category = self.request.query_params.get("category")
        # 分辨率
        resolution = self.request.query_params.get("resolution")
        if category:
            queryset = queryset.filter(category=category)
        if resolution == "1K":
            queryset = queryset.filter(resolution__lt="1280x720")
        elif resolution == "2K":
            queryset = queryset.filter(
                resolution__gte="1280x720", resolution__lt="2560x1440"
            )
        elif resolution == "4K":
            queryset = queryset.filter(
                resolution__gte="2560x1440", resolution__lt="3840x2160"
            )
        elif resolution == "8K":
            queryset = queryset.filter(
                resolution__gte="3840x2160", resolution__lt="7680x4320"
            )
        elif resolution == "其他":
            queryset = queryset.filter(resolution__gte="7680x4320")
        return queryset

    def list(self, request, *args, **kwargs):
        """
        重写 list 方法以添加调试信息。
        """
        response = super().list(request, *args, **kwargs)
        response.data["debug"] = {
            "page_size": self.pagination_class.page_size,
            "total_items": self.get_queryset().count(),
        }
        return response
