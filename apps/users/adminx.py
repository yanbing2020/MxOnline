# _*_coding: utf-8 _*_
import xadmin
from .models import EmailVerifyRecord, Banner
__data__ = '2017/7/17 16:22'


class EmailVerifyRecordAdmin(object):
    # list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    pass


class BannerAdmin(object):
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
