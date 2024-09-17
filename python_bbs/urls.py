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

    # 开始实现配置我们的media,实现暴露后端指定文件资源,就是前端可以实现的是通过网址来实现获取我们的文件资源
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]
