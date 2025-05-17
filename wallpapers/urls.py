from django.urls import path
from . import views


urlpatterns = [
    path("bulk-upload/", views.BulkUploadView.as_view()),
    # 分页
    path("wallpapers/page/", views.WallpaperListView.as_view(), name="wallpaper_page"),
    # 搜索
    path(
        "wallpapers/search/",
        views.WallpaperSearchView.as_view(),
        name="wallpaper_search",
    ),
    # 下载
    path(
        "wallpapers/download/<int:pk>/",
        views.WallpaperDownloadView.as_view(),
        name="wallpaper_download",
    ),
]
