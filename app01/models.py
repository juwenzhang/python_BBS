from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# 开始实现创建数据库的模型类

# 开始实现书写我们的用户的类
class UserInfo(AbstractUser):
    # 手机号
    phone = models.BigIntegerField(verbose_name="手机号", null=True, blank=True)
    # 头像，实现的是我们的上传都行到我们的这个目录下
    avatar = models.FileField(upload_to="avatar/", default="avatar/default.png", verbose_name="上传头像")
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 开始添加外键字段: 用户和个人站点之间是一对一的关系
    blog = models.OneToOneField(to="Blog", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


# 开始个人站点表的设计
class Blog(models.Model):
    site_name = models.CharField(max_length=32, verbose_name="站点名称")
    site_title = models.CharField(max_length=64, verbose_name="站点标题")
    # 实现传入的是我们的CSS或者说是JS 的文件路径即可
    site_theme = models.CharField(max_length=64, verbose_name="站点样式")

    def __str__(self):
        return self.site_name



# 文章分类表
class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name="文章分类")
    # 个人站点和文章分类之间是一对多关系
    blog = models.ForeignKey(to="Blog", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name


# 文章标签
class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="文章标签")
    blog = models.ForeignKey(to="Blog", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name


# 文章表
class Article(models.Model):
    title = models.CharField(max_length=64, verbose_name="文章标题")
    desc = models.CharField(max_length=255, verbose_name="文章简介")
    content = models.TextField(verbose_name="文章内容")
    create_time = models.DateTimeField(auto_now_add=True)
    up_time = models.BigIntegerField(verbose_name="点赞数", default=0)
    down_num = models.BigIntegerField(verbose_name="点睬数", default=0)
    comment_num = models.BigIntegerField(verbose_name="评论数", default=0)
    # 个人站点和文章之间是一对多关系
    blog = models.ForeignKey(to="Blog", on_delete=models.CASCADE, null=True, blank=True)
    # 文章和标签是多对多关系
    tags = models.ManyToManyField(to="Tag")
    # 文章和分类是一对多关系
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title


# 点赞点睬表
class UpAndDown(models.Model):
    # 这个就需要链接外键字段，同时删除方式是只要一点击，那么关于对应的表的数据就直接清空
    user = models.ForeignKey(to="UserInfo", on_delete=models.CASCADE)
    article = models.ForeignKey(to="Article", on_delete=models.CASCADE)
    is_up = models.BooleanField(default=False)


# 评论表
class Comment(models.Model):
    user = models.ForeignKey(to="UserInfo", on_delete=models.CASCADE)
    article = models.ForeignKey(to="Article", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="评论内容")
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    # 自关联字段
    parent = models.ForeignKey(to="self", on_delete=models.CASCADE)
