from django.urls import path
from . import views


urlpatterns = [
    path("wallpapers/", views.WallpaperListCreate.as_view()),
    path("wallpapers/<int:pk>/", views.WallpaperDetail.as_view()),
    path("bulk-upload/", views.BulkUploadView.as_view()),
    # 分页
    path("wallpapers/page/", views.WallpaperListView.as_view(), name="wallpaper_page"),
]
