# _*_coding: utf-8 _*_

import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner
__data__ = '2017/7/17 16:22'


class GlobalSetting(object):
    site_title = "慕学后台管理系统"
    site_footer = "墓学在线网"
    menu_style = "accordion"


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


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
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
