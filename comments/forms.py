from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    #在子类的定义中，表明对应的数据库模型，之后填写对应的需要填写的内容
    class Meta:
        model = Comment
        #fields会将填入的字段自动设置为类的属性
        fields = ['name', 'email', 'url', 'text']
