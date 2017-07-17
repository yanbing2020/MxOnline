# _*_coding: utf-8 _*_
from django import forms

__data__ = '2017/7/18 13:59'


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
