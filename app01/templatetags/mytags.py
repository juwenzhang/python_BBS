# 开始实现我们的书写我们的全局需要实现使用的一些从数据库中获取得到的数据
from django import template
from django.shortcuts import render
from app01 import models
from django.db.models import Count
from django.db.models.functions import TruncMonth


register = template.Library()

@register.inclusion_tag('left_menu.html')
def left_menu(username):
    # 开始实现通过我们的username来实现获取我们的用户对象
    user_obj = models.UserInfo.objects.filter(username=username).first()
    # 开始实现获取我们个人站点欣信息
    blog = user_obj.blog
    # 开始实现使用我们的所需要的数据参数有哪些进行书写
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
    # 然后实现的就是将我们的这个数据实现返回即可
    return locals()