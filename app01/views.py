from django.shortcuts import render
from app01.myforms.myforms import MyRegisterForm

# Create your views here.

# 实现注册的视图函数
def Register(request):
    # 先实例化我们的自定义form组件
    form_obj = MyRegisterForm()
    return render(request, "register.html", locals())