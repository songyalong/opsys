# coding:utf-8
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from ..common.login_out import *
from ..services.base import MenusService
from ..services.user import *


@csrf_exempt
def login_in(request):
    if request.method == "GET":
        return render_to_response("sign-in.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
<<<<<<< HEAD
        menus = MenusService.get_menus()
        if not username and not password:
            return render_to_response("index.html", {"menus": menus})
        else:
            return render_to_response("index.html", {"menus": menus})
=======
        if username and password:
            is_login = UserService.login_user_check(username, password, request.session)
            if is_login:
                request.session["username"] = username
                request.session["password"] = password
                menus = MenusService.get_menus()
                request.session["menus"] = menus
                return HttpResponseRedirect('/opsys/index/')
            else:
                message = "用户名和密码不匹配，请重新输入！"
        else:
            message = "用户名和密码不能为空，请重新输入！"
        return render_to_response("sign-in.html", {"message": message})


@login_required('index.html')
def index(request):
    """
    首页
    """
    if request.method == 'GET':
        param = {"messages": "欢迎使用opsys系统！"}
        return param
>>>>>>> dev
