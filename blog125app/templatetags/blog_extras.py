#定义模板标签
from django import template

from ..models import Post, Category, Tag

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    #显示按照最新时间排序取num个
    return {
        'recent_post_list': Post.objects.all().order_by('-created_time')[:num],
    }

@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    #一个是 created_time ，即 Post 的创建时间，month 是精度，order='DESC' 表明降序排列（即离当前越近的时间越排在前面）
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),
    }

@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }

@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }

