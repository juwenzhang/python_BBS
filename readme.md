# 开发项目的流程和注意事项

## 1.使用的开发框架
```angular2html
在本次的项目中
后端的使用的语言选择是python 
使用的开发框架是：
后端: django
前端: jquery    

前端使用组件库: bootstrap组件库
```

## 2.注册功能的实现
```angular2html
实现的步骤含有前端页面的搭建
以及通过jquery来实现的获取DOM，来实现我们的操作前端界面
通过ajax来实现提交前端数据给后端
同时后端也是需要给前端传递成功和报错的信息，返回给前端即可
```

## 3.登录界面的实现
```angular2html
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


https://www.zhaozi.cn/

CSRF_COOKIE_SECURE 设置为 True，这样 CSRF Cookies 就只会通过 HTTPS 发送

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

注意我们在实现登录的时候，我们的那个验证码的输入，关于含有字母的全部输入小写，否则就可能出现验证码错误的信息提示
这个小的bug我们后面在实现解决即可
```

## 4.首页具体的功能的实现
```angular2html
首页首先具有的功能就是我们的导航栏的实现
然后我们的导航栏的功能实现就是通过我们的model模态框来实现的，模态框原生实现的思路就是
z-index 属性来控制我们的不同的盒子的显示层级即可
但是我们这里是直接实现使用的我们的bootstrap 的javascript的组件库来直接实现的，有需要的直接按照这个流程来书写原生代码即可

```

## 5.个人站点的功能的完善
```angular2html
首先我们的个人站点的实现的时候，我们需要进行的是我们的一些保持原有的首页的导航栏的功能
然后我们需要实现的就是我们的个人站点的一些特有的主要内容区域的实现
同时我们这里的实现的是我们的基本的一些个人站点展示我们的个人的文章以及点击文章后我们实现的就是展示文章的主要内容
就是我们的content区域
后期的优化就是我们的会通过我们的一个input框来实现我们的搜索框的基本的功能
搜索框的实现的时候，搜索的内容就是根据我们的文章的标题来实现我们的内容的搜索
这个搜索框的实现就是通过的我们的ajax来实现发送请求，来实现我们的页面的局部的刷新
然后返回数据给前端实现渲染页面即可
```

## 6.使用django的内置的一些方法来实现我们网页的简写
```angular2html
就是我们是可以实现的是我们的通过我们的django的一些内置的模板继承以及那个全局的templatetags来实现我们的模板继承的写法
来实现我们的最基本的一些简写的操作
实现的步骤就是我们先在我们的应用目录下面实现我们的创建一个用来实现我们的全局的一些配置
然后直接使用我们的load方法来实现我们的加载我们的这个全局数据即可
这个就是我们django的模板语法的使用的基本的知识
这个也是我们的前后端未分离前的写法
但是我们是可以实现的是通过当下的前后端分离后的写法来实现书写

模板语法开发时候的查看: https://www.cnblogs.com/ssrheart/p/18067114
通过我们的边看文档边实现我们的开发，然后在抽离出自己喜欢使用就可以了
```


## 开发的时候的注意事项
```angular2html
我们实现开发的时候尤其注意的是解决我们的
csrf_token: 的伪造网站的问题  CSRF_COOKIE_SECURE = True
time_zone 的配置问题 :以及一些关于我们的连接服务器的时候的时间不匹配的问题就是我们的 time_zone 的配置问题

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

注意我们的配置项的修改，否则就可能导致我们的时间区域的问题，只要涉及到了时间方面的处理
```


## 前端向后端发送请求的方法
```angular2html
经常使用的含有: 
ajax 就是原生的一个网路的请求方法
axios 就是一个基于的ajax+promise的请求方式
fetch
request
```

## 拉取远程项目的方法
```angular2html
首先我们需要首先的是我们的项目从远程的github上面实现拉取下来
通过https拉取项目: git clone https://github.com/juwenzhang/python_BBS.git
通过SSH拉取项目: git clone git@github.com:juwenzhang/python_BBS.git
我的建议是先实现自己的 fork 项目
如果有什么值得修改的地方直接修改即可，修改后直接:
git add . 将修改的文件实现全部提交
git commit -m "提交的描述信息" 
git push -u origin branch_name 推送远程
gitk 查看自己的提交信息
最后在github官网上面实现我们的 pull request(PR)
作者自己了解了你的新的提交，感觉对自己的项目有用，那么就会同意你的合并请求
```

## 讲解项目
```angular2html
首先我们实现我们的项目的时候，。还是使用的以前的老的开发框架和我们的老的组件库
为什么会这样子耶？
是因为我们的项目本身原本就是为了实现我们的后面的对vue和react框架的更加深入的了解
每一个框架的每一个变迁的工作流程都是这样子的，没有任何的变动
大体的功能以及大体的工作的流程都是这样的

如果想要了解使用我们的组件库的话我们的前端的推荐有:
elementPlus  https://element-plus.org/zh-CN/
ant-design  https://ant-design.antgroup.com/index-cn?utm_source=xunbaodui  
bootstrap  https://www.bootcss.com/
dataV  https://datav.jiaminghi.com/
echarts https://echarts.apache.org/zh/index.html

推荐使用的前端开发框架
vue2/3  https://cn.vuejs.org/
react  https://react.xiniushu.com/
jquery  https://www.jquery123.com/
angular  https://v13.angular.io/docs


如果需要后期的项目的进阶，可以了解一哈具体的前端工程化开发流程
基本的流程就是含有:
1.eslint 的配置 这个的配置就是实现的是我们的具体的代码的质量的检查
2.prettier 的配置 这个就是对我们的代码的格式的检查
3.package.json 文件的使用，这个就是我们的前端项目的工程话开发的重要文件
4.husky 的配置 这个就是实现的是我们的代码通过git提交远程仓库的时候的配置问题
5.commitlint的配置 这个就是为了实现我们的git代码提交远程仓库的时候的提交规范的约束
6.stylelint的配置 这个就是为了实现我们的前端CSS样式的书写的规范性的实现

前端最重要的还是我们的node的环境的安装，有了这个我们的前端部分的代码才可以实现上面的工程化配置
安装了node了之后，我们的电脑就会自带一个 npm
npm 可以实现的就是我们的项目的工程化的初始化 npm init -->生成我们的 package.json 文件
npm install 这个就可以实现我们的安装我们的前端的工程化开发的依赖包
```

## 实现启动项目
```angular2html
我们实现启动我们的项目的时候，我们的后端语言的选择是我们的Python的django web 开发框架
实现启动项目的流程是
首先打开终端，输入我们的指令: python manage.py runserver
如果在启动项目的过程中发现启动具有不成功，请检查自己的路径是否正确

我们实现创建的超级用户的方法就是: python manage.py createsuperuser
然后后面的操作就是我们的输入 用户名(必选项)、密码(必选项)、邮箱(不是必选项) 
本次项目的超级用户账号以及密码为:
```


```angular2html
还有很多的收尾工作没做，直接烂尾吧，后面无聊了再改改 
真心不想写了

主要是我们的后台管理的功能以及首页的页面的功能还差很多，但是现在不想写了，后面再来
```
