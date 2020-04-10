from django.shortcuts import render, get_object_or_404
from  .models import Post, Category, Tag
#一种文本转化，可以将文本美化为HTML文本
import markdown
#添加正则
import re
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

# Create your views here.

def index(request):
    #post_list = Post.objects.all().order_by('-created_time')
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #extra 本身包含很多基础拓展，而 codehilite 是语法高亮拓展，这为后面的实现代码高亮功能提供基础，而 toc 则允许自动生成目录
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        #'markdown.extensions.toc',简易目录，没有修饰锚点
        TocExtension(slugify=slugify),
    ])
    #convert 方法将 post.body 中的 Markdown 文本解析成 HTML 文本，随后实例会多出来一个toc属性
    post.body = md.convert(post.body)
    #使用正则表达式来判断m是否为空
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})

#时间归档页面
def archive(request, year, month):
    #Python 中调用属性的方式通常是 created_time.year，但是由于这里作为方法的参数列表，
    # 所以 django 要求我们把点替换成了两个下划线，即 created_time__year
    #后一个year是输入的值，前面的created_time__year 是指post的属性
    #post_list = Post.objects.filter(created_time__year=year,created_time__month=month).order_by('-created_time')
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    )
    return render(request, 'blog/index.html', context={'post_list': post_list})

#分类界面
def category(request, pk):
    # 在类中查找pk值，相同的分类
    cate = get_object_or_404(Category, pk=pk)
    #根据分类查找post
    #post_list = Post.objects.filter(category=cate).order_by('-created_time')
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})

def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    #post_list = Post.objects.filter(tags=t).order_by('-created_time')
    post_list = Post.objects.filter(tags=t)
    return render(request, 'blog/index.html', context={'post_list': post_list})




