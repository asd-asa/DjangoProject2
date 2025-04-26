from django.http import JsonResponse
from django.views import View
from rest_framework_jwt.settings import api_settings
import json
from user.models import SysUser
from user.serializers import SysUserSerializer


class LoginView(View):
    def post(self, request):
        username = request.GET.get("username")
        password = request.GET.get("password")
        try:
            user = SysUser.objects.get(username=username, password=password)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            # 将用户对象传递进去，获取该用户的属性
            payload = jwt_payload_handler(user)
            # 生成token
            token = jwt_encode_handler(payload)
        except Exception as e:
            print(e)
            return JsonResponse({"code": 400, "message": "用户名或密码错误"})
        return JsonResponse(
            {
                "code": 200,
                "token": token,
                "user": SysUserSerializer(user).data,
                "Info": "登录成功",
            }
        )


class TestView(View):
    def get(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        if token != "" and token != None:
            userlist_obj = SysUser.objects.all()
            print(userlist_obj, type(userlist_obj))
            userlist_dict = userlist_obj.values()  # 转存为字典
            userlist = list(userlist_dict)
            print(userlist)
            return JsonResponse({"code": 200, "data": userlist})
        else:
            return JsonResponse({"code": 400, "message": "token不能为空"})


class JwtTestView(View):
    def get(self, request):
        users = SysUser.objects.all()
        tokens = []
        # 生成载荷
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        # 将用户对象传递进去，获取该用户的属性
        payload = jwt_payload_handler(user)
        # 生成token
        token = jwt_encode_handler(payload)
        return JsonResponse({"code": 200, "token": token})


class RegisterView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
        except Exception as e:
            return JsonResponse({"code": 400, "message": "请求数据格式错误"})

        # 检查参数是否为空
        if not username or not password:
            return JsonResponse({"code": 400, "message": "用户名或密码不能为空"})
        # 检查用户名是否已存在
        if SysUser.objects.filter(username=username).exists():
            return JsonResponse({"code": 400, "message": "用户名已存在"})

        # 创建用户
        try:
            user = SysUser.objects.create(
                username=username,
                password=password,
            )
            return JsonResponse(
                {"code": 200, "message": "注册成功", "user_id": user.id}
            )
        except Exception as e:
            return JsonResponse({"code": 500, "message": "注册失败", "error": str(e)})
