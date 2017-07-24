# _*_coding_*_ utf-8

from django import forms

from operation.models import UserAsk

__date__ = '2017/7/25 17:55'


class UserAskForm(forms.ModelForm):
                # 新增的字段
    class Meta:  # 继承的字段
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']
