from django.db import models


class Wallpaper(models.Model):
    MEDIA_TYPES = (
        ("computer", "电脑壁纸"),
        ("mobile", "手机壁纸"),
        ("avatar", "头像"),
        ("unknown", "未分类"),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50)
    media_type = models.CharField(
        max_length=20, choices=MEDIA_TYPES, default="computer"
    )
    tags = models.JSONField(blank=True, default=list)
    upload_date = models.DateTimeField(auto_now_add=True)
    downloads = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="wallpapers/")
    image_url = models.ImageField(upload_to="yasuo/")
    resolution = models.CharField(max_length=20)

    def __str__(self):
        return self.title
