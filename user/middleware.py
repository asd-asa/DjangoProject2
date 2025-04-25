from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from jwt import ExpiredSignatureError, InvalidTokenError, PyJWTError
from rest_framework_jwt.settings import api_settings


class JWtAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 白名单
        # white_list = ["/user/login/"]
        # path = request.path
        # # 判断是否在白名单中
        # if path not in white_list and not path.startswith("/media/"):
        #     print("需要进行token验证")
        #     token = request.META.get("HTTP_AUTHORIZATION")
        #     print("token:", token)
        #     if not token:
        #         return JsonResponse(
        #             {"message": "未提供token，请登录后重试"}, status=401
        #         )
        #     try:
        #         jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
        #         jwt_decode_handler(token)
        #     except ExpiredSignatureError:
        #         return JsonResponse({"messages": "token过期，请重新登录"})
        #     except InvalidTokenError:
        #         return JsonResponse({"message": "token验证失败"})
        #     except PyJWTError:
        #         return JsonResponse({"message": "token验证异常"})
        #
        # else:
        #     print("不需要进行token验证")
        return None
