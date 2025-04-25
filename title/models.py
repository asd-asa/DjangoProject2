from django.db import models


class NavigationItem(models.Model):
    title = models.CharField(max_length=100)  # 导航项标题
    path = models.CharField(max_length=200)  # 导航项路径
    order = models.IntegerField(default=0)  # 导航项顺序
    icon = models.CharField(max_length=100, blank=True)  # 导航项图标

    class Meta:
        ordering = ["order"]  # 按照 order 字段排序

    def __str__(self):
        return self.title


class CategoryItem(models.Model):
    name = models.CharField(max_length=100)  # 分类名称
    resolution = models.CharField(max_length=20)  # 分辨率
    tags = models.CharField(max_length=200)  # 分类标签
    order = models.IntegerField(default=0)  # 分类顺序

    class Meta:
        ordering = ["order"]  # 按照 order 字段排序

    def __str__(self):
        return self.name


class CategoryList(models.Model):
    title = models.CharField(max_length=100)  # 分类列表标题
    order = models.IntegerField(default=0)  # 分辨率顺序

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
