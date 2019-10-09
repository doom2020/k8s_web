import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from k8sys.action import HomeViewHandle, LoginViewHandle, RegisterViewHandle



class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'basic2.html', locals())

    def post(self, request, *args, **kwargs):
        home_view_handle = HomeViewHandle(request)
        op_handle = home_view_handle.get_handle()
        ret_dict = op_handle()
        return HttpResponse(json.dumps(ret_dict))



class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, '', locals())

    def post(self, request, *args, **kwargs):
        login_view_handle = LoginViewHandle(request)
        op_handle = login_view_handle.get_handle()
        ret_dict = op_handle()
        return HttpResponse(json.dumps(ret_dict))



class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, '', locals())

    def post(self, request, *args, **kwargs):
        register_view_handle = RegisterViewHandle(request)
        op_handle = register_view_handle.get_handle()
        ret_dict = op_handle()
        return HttpResponse(json.dumps(ret_dict))

