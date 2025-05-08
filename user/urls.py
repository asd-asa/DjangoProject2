from django.contrib.auth import login
from django.urls import path


from user.views import LoginView, RegisterView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),  # 用户登录
    path("register/", RegisterView.as_view(), name="register"),  # 用户注册
]
