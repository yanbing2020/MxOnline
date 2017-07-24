# _*_coding_*_ utf-8
from django.conf.urls import url, include
from .views import OrgView, AddUserAskView

__date__ = '2017/7/25 18:07'


urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name="org_list"),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),

]
