# _*_coding_*_ utf-8
from django.conf.urls import url, include
from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourselView, OrgDescView, OrgTeacherView, AddFavView

__date__ = '2017/7/25 18:07'


urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name="org_list"),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),  # ajax 异步方式实现
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),
    url(r'^course/(?P<org_id>\d+)/$', OrgCourselView.as_view(), name="org_course"),
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="org_desc"),
    url(r'^teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name="org_teacher"),
    # 机构收藏
    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),  # ajax 异步方式实现
]
