# _*_coding: utf-8 _*_
from django import forms
from captcha.fields import CaptchaField

__data__ = '2017/7/18 13:59'


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(required=True, error_messages={"invalid": "验证码错误！"})  # (error_messages={"invalid": "验证码错误！"})

