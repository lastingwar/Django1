# Django框架的博客应用
#### 导语：
> [个人博客页面](http://106.12.33.2:5000/) 请直接打开网页观看。基于Django框架下的个人博客，用于记录个人学习中遇到的问题和资料。

## 一、部署服务器

项目部署于百度云服务器
![微信图片_20200411140116.png](https://i.loli.net/2020/04/11/Vej85EhfBHywJdA.png)
使用Gunicorn，启动 2 个 worker 用于处理请求，指定为 gthread 的异步模式能获取比较高的性能。
使用Nginx， (engine x) 是一个高性能的 HTTP 和反向代理 web 服务器
使用Supervisor控制项目后台运行，同时保证项目在出现偶然情况下能自动重启。
![微信图片_20200411174731.png](https://i.loli.net/2020/04/11/FzZ1jVLJAOImyuc.png)

## 二、登录

通过admin界面登入后台系统
![微信图片_20200411135329.png](https://i.loli.net/2020/04/11/U47LFyN96nogmk5.png)

## 三、发布文章

进入到admin界面之后，通过页面进行内容的添加和发布
![微信图片_20200411135523.png](https://i.loli.net/2020/04/11/Jw6Tsy2hbEAdNRg.png)

## 四、查看页面

[个人博客页面](http://106.12.33.2:5000/)通过网址直接进入到外网界面，根据标签查询内容。

![微信图片_20200411103107.png](https://i.loli.net/2020/04/11/RpJFLBmsqVoGuMe.png)

## 五、拓展功能

目前博客添加有评论功能，后续会不断进行更新和优化。

![微信图片_20200411103110.png](https://i.loli.net/2020/04/11/nhji9plCtarIv6d.png)


