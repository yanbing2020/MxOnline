# _*_coding_*_ utf-8

from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView, CourseInfoView

__date__ = '2017/7/30 12:19'

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    url(r'^detail/(?P<course_id>\d+)$', CourseDetailView.as_view(), name="course_detail"),
    url(r'^info/(?P<course_id>\d+)$', CourseInfoView.as_view(), name="course_info"),
]