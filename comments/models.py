from django.db import models
from django.utils import timezone

#评论的数据库模型
class Comment(models.Model):
    #verbose_name 是后台的名称，一般为第一个参数，副键和多对多关系中，需要用关键字参数指出
    name = models.CharField('名字', max_length=50)
    email = models.EmailField('邮箱')
    url = models.URLField('网址', blank=True)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    post = models.ForeignKey('blog125app.Post', verbose_name='文章', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])