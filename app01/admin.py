from django.contrib import admin
from app01 import models

# Register your models here.
# 开始实现我们的项目的后台管理的实现书写admin
# 我们在这里是可以实现我们的给超级用户实现添加我们的给他定义的可以操作的模型表的有哪些的
admin.site.register(models.UserInfo)
admin.site.register(models.Blog)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Article)
admin.site.register(models.UpAndDown)
admin.site.register(models.Comment)