from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random
from app01 import models
from app01.myforms.myforms import MyRegisterForm
from django.contrib import auth
# 这个就是来实现我们的判断是否处于登录状态的一个登录验证器
from django.contrib.auth.decorators import login_required
from django.db.models import Count, F
from django.db.models.functions import TruncMonth
import json


# Create your views here.


# def set_time_zone():
#     with connection.cursor() as cursor:
#         cursor.execute("SET time_zone = 'UTC'")

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
        img_draw.text(((i + 1) * 28, 5), tem, fill=get_random_color(), font=img_font)
        code += tem
    # 通过随机验证码来实现我们的验证码的校验
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
        back_info = {"code": 200, "message": ""}
        # 开始实现我们的获取前端传递的数据
        username = request.POST.get("username")
        password = request.POST.get("password")
        code = request.POST.get("code")
        # 开始进行我们的校验验证码是否正确
        if request.session.get("code") == code:
            # 然后实现校验用户名以及密码
            user_obj = auth.authenticate(username=username, password=password)
            if user_obj:
                auth.login(request, user_obj)
                back_info["url"] = "/home/"
            else:
                back_info["code"] = 400
                back_info["message"] = "用户名或者密码错误..."
        else:
            back_info["code"] = 400
            back_info["message"] = "验证码错误..."
        return JsonResponse(back_info)
    return render(request, "login.html", locals())


# 开始书写我们的主页的视图函数
def home(request):
    # 开始实现获取所有的文章标题
    article_queryset = models.Article.objects.all()
    return render(request, "home.html", locals())


# 开始实现书写我们的修改密码的后端逻辑
@login_required
def set_password(request):
    # 我们这一步的实现的时候，使用的就是实现我们的模态栏的出现让用户实现修改
    # 通过我们的z-index 来实现我们的功能 https://baike.baidu.com/item/z-index/7662375?fr=ge_ala
    # 通过我们的 z-index 来实现我们的基本的迭代的实现，一层一层的实现 z-index 就是实现的不同的div 来实现我
    # 们的不同的div实现迭代框
    # 开始实现我们的获取前端的数据
    if request.method == "POST":
        back_info = {"code": 200, "message": "", "url": ""}
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        # 开始实现我们的数据的校验
        is_right = request.user.check_password(old_password)
        # print(request.user.password, is_right, old_password, new_password, confirm_password)
        if is_right:
            # 判断两次密码是否一致
            if new_password == confirm_password:
                request.user.set_password(new_password)
                request.user.save()
                back_info["message"] = "密码修改成功"
            else:
                back_info["code"] = 400
                back_info["message"] = "两次密码不一致..."
        else:
            back_info["code"] = 400
            back_info["message"] = "原密码错误..."
        return JsonResponse(back_info)


# 开始实现我们的退出登录的功能的实现
# 退出登录的时候，我们还是需要的是我们的处于登录状态才可以实现退出，否则就不用
@login_required
def logout(request):
    auth.logout(request)
    return redirect("/home/")


# 开始书写我们的个人站点的视图函数
# 我们的第三个参数的实现就是来实现的是我们的 那些选择参数的添加的实现
def user_site(request, username, **kwargs):
    # 这个时候我们的实现的就是username的是一个必选的参数，**kwargs 就是实现的是我们的接收我们的可选参数

    # 开始实现我们的当前的个人站点是否存在，否则就是我们的 404 NOT FOUND 页面实现返回
    user_obj = models.UserInfo.objects.filter(username=username).first()
    if not user_obj:
        # 这个时候我们的用户不存在，直接返回一个 404 NOT FOUND 的页面
        return render(request, "error.html", locals())
    blog = user_obj.blog
    # 开始实现查询我们的个人站点的含有的所有文章
    article_list = models.Article.objects.filter(blog=blog)

    # 开始实现我们对文章列表实现我们的再次筛选就是通过我们的最终的可选参数来实现的筛选
    if kwargs:
        # 开始实现我们的获取可选参数的值，当传入的这个有值的话
        # 通过我们的这个的实现的时候是通过通过我们的字典来实现的接收参数的
        condition = kwargs.get('condition')  # 这里只含有我们的三种情况 category |  tag  |  data
        param = kwargs.get('param')
        # 开始实现我们的对文章实现查询过滤
        if condition == "category":
            article_list = article_list.filter(category__id=param)
        elif condition == "tag":
            article_list = article_list.filter(tags__pk=param)
        else:
            year, month = param.split("-")
            article_list = article_list.filter(create_time__year=year, create_time__month=month)

    # 查询当前用户得分类以及分类下面得文章数目
    category_list = (models.Category.objects.filter(blog=blog).annotate(count_num=(Count('article__pk')))
                     .values_list('name', 'count_num', "pk"))
    # 查询当前用户得所有标签以及标签下得文章数
    tag_list = (models.Tag.objects.filter(blog=blog).annotate(count_num=(Count('article__pk')))
                .values_list('name', 'count_num', "pk"))
    # 按照年月统计文章以及数量
    data_list = ((models.Article.objects.filter(blog=blog).annotate(month=TruncMonth('create_time'))
                  .values('month')).annotate(count_num=(Count('pk')))
                 .values_list('month', 'count_num', "pk"))
    return render(request, "user_site.html", locals())


# 开始实现我们的获取我们的文章的详情页id
def article_detail(request, username, article_id):
    # 这个就是我们的文章的详情页的视图函数
    article_obj = models.Article.objects.filter(pk=article_id).first()
    blog = article_obj.blog
    user_name = username
    if not article_obj:
        return render(request, "error.html", locals())
    return render(request, "article_detail.html", locals())


# 开始书写我们的用来实现我们点赞点睬的后端视图函数
def up_or_down(request):
    back_info = {"code": 200, "message": ""}
    if request.method == "POST":
        # 判断是否处于登录
        if request.user.is_authenticated:
            article_id = request.POST.get("article_id")
            is_up = json.loads(request.POST.get("is_up"))
            # 判断当前文章是否是自己写的
            article_obj = models.Article.objects.filter(pk=article_id).first()
            if not article_obj.blog.userinfo == request.user:
                # 判断用户是否存在连续点击
                is_click = models.UpAndDown.objects.filter(user=request.user, article=article_obj)
                if not is_click:
                    # 操作数据库以及保存数据
                    # 判断用户是点了赞还是点了踩
                    if is_up:
                        models.Article.objects.filter(pk=article_id).update(up_num=F("up_num") + 1)
                        # 开始实现修改返回的描述信息
                        back_info["code"] = 200
                        back_info["message"] = "点赞成功..."
                    else:
                        models.Article.objects.filter(pk=article_id).update(down_num=F("down_num") + 1)
                        back_info["code"] = 200
                        back_info["message"] = "点睬成功..."
                    # 开始实现我们的给我们的一些点菜点赞表实现操作
                    models.UpAndDown.objects.filter(user=request.user, article=article_obj, is_up=is_up)
                # 存在逻辑问题哟
                else:
                    back_info["code"] = 400
                    back_info["message"] = "已点赞，不可重复点赞..."
            else:
                back_info["code"] = 400
                back_info["message"] = "是用户本人，用户本人不可给自己点赞..."
        else:
            back_info["code"] = 401
            back_info["message"] = "用户还未<a href='/login/'>登录</a>，请登录后再来操作..."
    return JsonResponse(back_info)


# 开始实现我们的评论功能的实现
def comment(request):
    if request.method == "POST":
        back_info = {"code": 200, "message": ""}