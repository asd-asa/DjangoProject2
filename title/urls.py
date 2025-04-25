from django.urls import path
from .views import NavigationBarView, CategoryItemView, CategoryListView

urlpatterns = [
    path(
        "navigation-bar/", NavigationBarView.as_view(), name="navigation_bar"
    ),  # 导航栏接口
    path(
        "category-item/", CategoryItemView.as_view(), name="category_item"
    ),  # 分类项接口
    path(
        "category-list/", CategoryListView.as_view(), name="category_list"
    ),  # 分类列表接口
]
