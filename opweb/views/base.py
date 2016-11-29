#coding:utf-8
from ..services.base import MenusService
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render_to_response
import json
from django.core.serializers import serialize

def get_menus(request):
    if request.method == "GET":
        return render_to_response(serialize('json', MenusService.get_menus()))