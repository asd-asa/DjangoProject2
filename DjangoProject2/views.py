from django.http import HttpResponse


def home_view(request):
    return HttpResponse("欢迎访问首页！")
