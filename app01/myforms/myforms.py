# 开始书写自己的form组件
from django import forms
from app01 import models

# 自定义一个注册功能的form组件
class MyRegisterForm(forms.Form):
    #  开始设置数据
    username = forms.CharField(label="用户名", max_length=8, min_length=3, required=True,
                               error_messages={
                                   'required': "用户名不可为空",
                                   'min_length': "用户名最少三位",
                                   'max_length': "用户名最多八位"
                               },
                               widget=forms.TextInput(attrs={"class": "form-control"})
                               )

    password = forms.CharField(label="密码", max_length=20, min_length=8, required=True,
                               error_messages={
                                   'required': "密码不可为空",
                                   'min_length': "密码最少八位",
                                   'max_length': "密码最多二十位"
                               },
                               widget=forms.PasswordInput(attrs={"class": "form-control"})
                               )

    confirmPassword = forms.CharField(label="确认密码", max_length=20, min_length=8, required=True,
                                      error_messages={
                                          'required': "不可为空",
                                          'min_length': "密码最少八位",
                                          'max_length': "密码最多二十位"
                                      },
                                      widget=forms.PasswordInput(attrs={"class": "form-control"})
                                      )

    email = forms.EmailField(label="邮箱", error_messages={
                                "required": "邮箱不可为空",
                                "invalid": "邮箱格式出错"
                            },
                            widget=forms.EmailInput(attrs={"class": "form-control"})
                            )

    #  下面的钩子函数是用来实现我们的注册功能的时候的密码和用户名的校验

    # 开始实现书写钩子函数
    # 局部钩子: 实现校验用户名是否存在
    def clean_username(self):
        username = self.cleaned_data.get('username')
        res = models.UserInfo.objects.filter(username=username)
        if res:
            self.add_error("username", '用户名已存在，请重新输入用户名')
        return username

    # 全局钩子: 判断用户输入的两次密码是否一致
    def clean(self):
        cleaned_data = super(MyRegisterForm, self).clean()
        password = self.cleaned_data.get('password')
        confirmPassword = self.cleaned_data.get('confirmPassword')
        if not password == confirmPassword:
            self.add_error('confirmPassword', "两次密码不一致")
        return cleaned_data