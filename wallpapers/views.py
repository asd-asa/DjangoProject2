from PIL import Image
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Wallpaper
from .serializers import WallpaperSerializer, WallpaperPagination
from rest_framework.permissions import IsAuthenticated


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
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        # 检查 Authorization 头部
        auth_header = get_authorization_header(request).split()
        if not auth_header or auth_header[0].lower() != b"bearer":
            raise AuthenticationFailed("Authorization header missing or invalid")

        token = auth_header[1]

        files = request.FILES.getlist("images")
        created_data = []

        for img in files:
            try:
                # 使用 Pillow 获取图片宽度和高度
                image = Image.open(img)
                width, height = image.size

                # 生成压缩图片
                image_url = image.copy()

                compressed_io = BytesIO()
                if img.name.lower().endswith(".png"):
                    image_url.save(
                        compressed_io, format="PNG", optimize=True, quality=85
                    )
                else:
                    image_url.save(compressed_io, format="JPEG", quality=75)
                    # 生成唯一文件名
                    unique_name = f"{uuid.uuid4().hex[:10]}_{img.name}"
                    compressed_file = ContentFile(
                        compressed_io.getvalue(), name=f"compressed_{unique_name}"
                    )
                    original_file = ContentFile(
                        img.read(), name=f"original_{unique_name}"
                    )
                # 创建 Wallpaper 对象
                wallpaper = Wallpaper.objects.create(
                    title=request.POST.get(
                        "title", img.name.split(".")[0]
                    ),  # 从 POST 获取标题
                    image=original_file,
                    image_url=compressed_file,  # 使用压缩后的图片
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
