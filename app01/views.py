from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random
from app01 import models
from app01.myforms.myforms import MyRegisterForm
from django.contrib import auth

# Create your views here.

# 实现注册的视图函数
def Register(request):
    # 通过我们的返回的code的值给前端进行判断即可
    # 先实例化我们的自定义form组件
    form_obj = MyRegisterForm()
    # 开始实现后端操作前端数据入数据库
    if request.method == 'POST':
        back_info = {"code": 200, "message": "注册成功"}
        # 通过我们的额内置的form组件来实现校验数据是否合法
        form_obj = MyRegisterForm(request.POST)
        if form_obj.is_valid():
            clean_data = form_obj.cleaned_data
            # print(cleaned_data)
            # 开始实现我们的将确认密码的键值对实现删除
            # 确保 clean_data 是一个字典
            if isinstance(clean_data, dict):
                # 开始实现我们的将确认密码的键值对实现删除
                clean_data.pop("confirmPassword", None)
                user_avatar = request.FILES.get("avatar")
                # 判断是否获取到用户头像
                if user_avatar:
                    clean_data["avatar"] = user_avatar
                # 然后开始直接实现我们的传入数据入数据库
                models.UserInfo.objects.create_user(**clean_data)
                back_info["url"] = "/login/"
                # print(back_info)
        else:
            back_info["code"] = 400
            back_info["message"] = form_obj.errors
            # back_info["url"] = "/error/"
        return JsonResponse(back_info)
    return render(request, "register.html", locals())


# 开始实现我们的随机生成颜色的视图函数的书写
def get_random_color():
    # 颜色的更改就是实现的是我们的三原色的随机更改（就是实现的是随机生成三个数字即可）
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def get_code(request):
    # img_obj = Image.new("RGB", (200, 40), get_random_color())
    # # 实现将我们的图片实现保存
    # with open("static/images/code.png", "wb") as f:
    #     img_obj.save(f, format="PNG")
    # # 然后实现我们的读取文件返回给前端
    # with open("static/images/code.png", "rb") as f:
    #     img_data = f.read()
    # return HttpResponse(img_data, content_type="image/png")

    # 实现产生图片
    img_obj = Image.new("RGB", (200, 40), get_random_color())
    # 实现产生一个画笔出来
    img_draw = ImageDraw.Draw(img_obj)
    # 生成一个用于作画的字体
    img_font = ImageFont.truetype("static/fonts/001.ttf", 30)
    # 开始实现随机生成验证码
    code = ""
    for i in range(6):
        random_upper = chr(random.randint(65, 90))  # 生成随机的大写字母
        random_lower = chr(random.randint(97, 122))  # 实现的是生成小写字母
        random_int = random.randint(0, 9)
        # 实现随机选择上面的一个值
        tem = random.choice([random_upper, random_lower, str(random_int)])
        # img_draw.text(坐标， 字符， 颜色， 字体样式)
        img_draw.text(((i+1)*28, 5), tem, fill=get_random_color(), font=img_font)
        code += tem
    # 通过随机验证码来实现我们的验证码的校验
    # print(len(code))
    # print(code.lower())
    # 有的时候我们实现的生成的验证码是看不清楚的，这个时候就需要我们前端通过我们的点击事件发送ajax请求来实现变更验证码
    # 前端就实现了我们的验证码的局部刷新，这个就是我们的ajax的特点之一，实现页面的局部刷新的特点
    request.session["code"] = code.lower()
    # 创建一个io管理器出来
    io_obj = BytesIO()
    img_obj.save(io_obj, format="PNG")
    return HttpResponse(io_obj.getvalue(), content_type="image/png")


# 实现登录页面的视图函数
def Login(request):
    if request.method == "POST":
        back_info = {"code": 200, "message": "登录成功"}
        # 开始实现设置我们的前端传递给后端的数据
        username = request.POST.get("username")
        password = request.POST.get("password")
        code = request.POST.get("code")
        # 先实现校验我们的验证码是否正确（我们不需要实现区分大小写）
        # 存在bug
        print(code)
        if request.session["code"] == str(code).lower():
            # 然后实现校验用户名是否存在以及密码是否正确
            user_obj = auth.authenticate(request, username=username, password=password)
            if user_obj:
                # 保存用户的登录状态，同时返回项目的home界面
                auth.login(request, user_obj)
                back_info["url"] = "/home/"
            else:
                back_info["code"] = 400
                back_info["message"] = "用户名或者密码错误..."
        else:
            back_info["code"] = 401
            back_info['message'] = "验证码错误..."
        return JsonResponse(back_info)
    return render(request, "login.html", locals())


# 开始书写我们的主页的视图函数

def home(request):
    return render(request, "home.html")