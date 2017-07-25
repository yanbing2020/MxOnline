# _*_coding_*_ utf-8

from django import forms
import re

from operation.models import UserAsk

__date__ = '2017/7/25 17:55'


class UserAskForm(forms.ModelForm):
                # 新增的字段
    class Meta:  # 继承的字段
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        验证手机号码是否合法
        """
        mobile = self.cleaned_data['mobile']
        REGREX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|176\d{8}$"
        p = re.compile(REGREX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码非法", code="mobile_invalid")


