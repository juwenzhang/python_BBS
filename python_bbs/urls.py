"""python_bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app01 import views
# 开始实现配置我们media
from python_bbs import settings
from django.views.static import serve

urlpatterns = [
    path("", views.redirect_page),
    path('admin/', admin.site.urls),
    #  实现注册功能
    path('register/', views.Register),
    # 开始配置登录
    path('login/', views.Login),
    # 开始是西安我们的验证码的操作
    path('get_code/', views.get_code),
    # 主页的页面
    path('home/', views.home),
    # 开始实现设置修改密码的操作
    path('set_password/', views.set_password),
    # 开始实现我们的退出登录功能的实现
    path('logout/', views.logout),
    # 开始实现书写我们的点赞点彩的路由路径
    path('up_or_down/', views.up_or_down),
    # 评论的功能的实现
    path('comment/', views.comment),
    # 后台管理
    path('backend/', views.backend),
    # 开始实现我们的添加文章
    path('add_article/', views.add_article),
    # 开始实现书写我们的文章编辑的页面
    re_path('article/edit/(?P<edit_id>\d+)', views.article_edit, name='article_edit'),
    # 开始实现我们的个人的姓名的实现书写
    re_path(r'^(?P<username>\w+)/$', views.user_site),
    # 开始我们的文章详情页
    re_path(r'^(?P<username>\w+)/article/(?P<article_id>\d+)/', views.article_detail),
    # 开始实现我们的侧边栏的筛选功能
    re_path(r'^(?P<username>\w+)/(?P<condition>category|tag|data)/(?P<param>.*)/', views.user_site),
    # re_path(r'^(?P<username>\w+)/category/(\w+)/', views.user_site),  # 文章分类
    # re_path(r'^(?P<username>\w+)/tag/(\w+)/', views.user_site),  # 文章标签
    # re_path(r'^(?P<username>\w+)/data/(\w+)/', views.user_site)  # 文章日期
    # 开始实现配置我们的media,实现暴露后端指定文件资源,就是前端可以实现的是通过网址来实现获取我们的文件资源
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]
