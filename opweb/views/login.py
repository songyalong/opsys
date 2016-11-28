# coding:utf-8
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from ..common.login_out import *

"""登录页面"""
@csrf_exempt
def login_in(request):
    if request.method == "GET":
        return render_to_response("sign-in.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username and not password:
            return render_to_response("index.html")
        else:
            return render_to_response("index.html")


"""登出"""
def login_out(request):
    pass
