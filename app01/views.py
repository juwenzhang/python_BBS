from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

# 实现操作我们的图片链接的时候，我们需要的是下面的三个类函数
from PIL import Image, ImageDraw, ImageFont
# 开始实现我们的存储图片
from io import BytesIO, StringIO

from app01 import models
from app01.myforms.myforms import MyRegisterForm


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


# 实现登录页面的视图函数
def Login(request):
    return render(request, "login.html", locals())


# 使用我们的pillow来实现操作我们的图片
# 书写获取验证码的视图函数
"""
from PIL import Image, ImageDraw, ImageFont
image  就是实现的是我们的生成图片
ImageDraw 就是在图片上面实现可以画图
ImageFont 实现的就是我们的在图片上实现书写我们的字体

实现的图片的保存放置于我们的内存中，不需要我们的占用内置的空间
from io import BytesIO, StringIO
ByteIO 实现的是临时存储数据,返回的是我们的二进制格式
StringIO 实现的是临时存储数据,返回的是我们的字符串格式

"""


def get_code(request):
    img_obj = Image.new("RGB", (200, 40), "white")
    # 实现将我们的图片实现保存
    with open("static/images/code.png", "wb") as f:
        img_obj.save(f, format="PNG")
    # 然后实现我们的读取文件返回给前端
    with open("static/images/code.png", "rb") as f:
        img_data = f.read()
    return HttpResponse(img_data, content_type="image/png")