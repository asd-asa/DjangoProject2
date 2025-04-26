from django.contrib.auth import login
from django.urls import path

from user.views import TestView, JwtTestView, LoginView, RegisterView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),  # 用户登录
    path("test/", TestView.as_view(), name="test"),
    path("jwttest/", JwtTestView.as_view(), name="jwttest"),
    path("register/", RegisterView.as_view(), name="register"),  # 用户注册
]
