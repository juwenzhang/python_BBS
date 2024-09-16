# 1.使用的开发框架
```angular2html
<div>
在本次的项目中
后端的使用的语言选择是python 
使用的开发框架是：
后端: django
前端: jquery    

前端使用组件库: bootstrap组件库    
</div>
```

# 2.注册功能的实现
```angular2html
<div>
实现的步骤含有前端页面的搭建
以及通过jquery来实现的获取DOM，来实现我们的操作前端界面
通过ajax来实现提交前端数据给后端
同时后端也是需要给前端传递成功和报错的信息，返回给前端即可
</div>
```

# 3.登录界面的实现
```angular2html
<div>
    在实现我们的登录页面的时候
后端需要进行处理的就是我们的生成随机的验证码的操作以及存储生成的随机的验证码的操作的思路
同时还有需要的是将我们的生成的随机的验证码图片进行存储的的基本的格式要求
实现的是我们的不在本地实现存储，而是临时存储我们的数据
同时我们实现的时候，需要实施的就是通过一个视图函数来实现获取随机验证码

`from PIL import Image, ImageDraw, ImageFont`
image  就是实现的是我们的生成图片
ImageDraw 就是在图片上面实现可以画图
ImageFont 实现的就是我们的在图片上实现书写我们的字体

实现的图片的保存放置于我们的内存中，不需要我们的占用内置的空间
`from io import BytesIO, StringIO`
ByteIO 实现的是临时存储数据,返回的是我们的二进制格式
StringIO 实现的是临时存储数据,返回的是我们的字符串格式

同时为了我们的每次生成的验证码的字体的不同，我们可以直接上找字网中寻找实现下载即可
然后我们的随机验证码的生成的时候，我们的实现是通过我们的最终的: `大写字母` + `小写字母` + `数字` 随机组成的    
</div>

<a>https://www.zhaozi.cn/</a>

<p>CSRF_COOKIE_SECURE 设置为 True，这样 CSRF Cookies 就只会通过 HTTPS 发送</p>

前端处理cookie的函数
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
```