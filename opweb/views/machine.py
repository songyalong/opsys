#coding:utf-8
from django.views.decorators.csrf import csrf_exempt
from ..services.machine import MachineService
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def machine_list(request):
    if request.method == "GET":
        machine_list = MachineService.get_all_machine()
        return JsonResponse("machine_list.html", {"machine_list": machine_list})
    elif request.method == "POST":
        pass