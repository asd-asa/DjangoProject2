from django.db import models


class Wallpaper(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50)
    tags = models.JSONField(blank=True, default=list)
    upload_date = models.DateTimeField(auto_now_add=True)
    downloads = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="wallpapers/")
    image_url = models.ImageField(upload_to="yasuo/")
    resolution = models.CharField(max_length=20)

    def __str__(self):
        return self.title
