# _*_coding_*_ utf-8

from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView

__date__ = '2017/7/30 12:19'

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    url(r'^detail/(?P<course_id>\d+)$', CourseDetailView.as_view(), name="course_detail"),
]