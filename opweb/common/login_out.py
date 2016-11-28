# coding:utf-8
import functools


def is_login(request):
    def decro_is_login(func):
        @functools.wraps(func)
        def wraps(*args, **keyvalues):
            print "session"
            return func(*args, **keyvalues)

        return wraps

    return decro_is_login


#__author__ = 'K'
# coding: utf-8
import json

from django.http import HttpResponse

from common.utils.json_config import json_service_error, json_request_error


def login_required(html):
    def _login_required(func):
        def __deco(*args, **kwargs):
            ret = func(*args, **kwargs)
            request = args[0]
            session = request.session
            #  判断是否登录
            if session.has_key('user'):
                if type(ret) is dict:
                    ret['menu'] = session.get('menu')
                    ret['user'] = session.get('user')
                    ret['is_superuser'] = session.get('user').get('is_superuser')
                    current_location = request.REQUEST.get('current_location')
                    if not ret.has_key('current_location'):
                        ret['current_location'] = current_location
                    ret['menu_no'] = request.REQUEST.get('menu_no')
                    response = generic_template(html, ret)
                    return HttpResponse(response)
                else:
                    return ret
            else:
                #  添加HttpResponse header
                if type(ret) is dict:
                    local_html = 'login.html'
                    response = generic_template(local_html, {})
                    return HttpResponse(response)
        return __deco
    return _login_required


def menu_auth(html):
    """
    admin auth 返回每个用户的权限
    """
    def _menu_auth(func):
        def __menu_auth(*args, **kwargs):
            request = args[0]
            param = func(*args, **kwargs)
            if param is dict:
                #  统一给后台view加上用户权限以及用户
                param['menu'] = request.session.get('menu')
                param['user'] = request.session.get('user')
                response = generic_template(html, param)
                return HttpResponse(response)
            else:
                return param
        return __menu_auth
    return _menu_auth


def argument_check(argument, method, type='body'):
    """
    api请求方式检查
    api接口必传参数检查
    @param: argument 必传参数list tuple都可以
    @param: method 请求方法get,post ['GET', 'POST'] list
    @param: type form-data还是get参数还是body参数
    @return: 提示客户端参数错误json
    {
        "status": 405,
        "message":  anything argument is not null
        "objects": null
    }
    """
    def _argument(func):
        def __argument(*args, **kwargs):
            #  request obj
            request = args[0]
            #  请求接口方式
            request_method = request.method
            #  支持多种method请求
            method_str = ''
            for m in method:
                method_str += m + ","
                m.upper()
            #  接口支持请求方式
            if request_method.upper() not in method:
                request_error_dict = json_request_error()
                request_error_dict['message'] = request_method + '请求！此接口只支持'+method_str+'请求!'
                return api_return(request, request_error_dict)
            argument_dict = dict()
            argument_dict['status'] = 405
            argument_dict['objects'] = None
            # 根据method不同检查相对应参数
            check_argument_is_null, return_argument_dict = check_argument(argument, request, argument_dict, method)
            if check_argument_is_null:
                return api_return(request, return_argument_dict)
            ret = func(*args, **kwargs)
            #  添加HttpResponse header
            return HttpResponse(ret)
        return __argument
    return _argument


def check_argument(argument, request, argument_dict, method):
    """
    根据请求方式不同检查参数
    @param: argument 需要检查参数list or tuple
    @param: request django request
    @param: argument_dict 返回字典信息
    @param: method 请求方式
    @return: boolean 是否有不正确参数
    """
    check_argument_is_null = False
    #  保存参数为None的list
    argument_is_none = []
    #  遍历必须传参数list或者tuple
    for a in argument:
        # 根据method获取参数值
        request_argument = request.REQUEST.get(a)
        if not request_argument or request_argument == '':
            argument_is_none.append(a)
            check_argument_is_null = True
    argument_is_none.append('参数不能为空')
    argument_dict['message'] = ', '.join(argument_is_none)
    return check_argument_is_null, argument_dict


def service_check(func):
    """
    捕捉service异常
    @return: 异常信息
    """
    def _service(*args, **kwargs):
        try:
            request = args[0]
            ret = func(*args, **kwargs)
        except Exception, e:
            service_error = json_service_error()
            service_error['message'] = str(e.message)
            return api_return(request, service_error)
        return ret
    return _service


def api_return(request, json_data):
    return HttpResponse(json.dumps(json_data, ensure_ascii=False))


from django.template import loader, Context


def generic_template(html, param):
    """
    html: 需要返回的html
    param: 字典类型需要传到html中的参数
    """
    template = loader.get_template(html)
    response_template = template.render(Context(param))
    return response_template

