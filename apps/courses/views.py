from django.http import HttpResponse

from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Course
from operation.models import UserFavorite, CourseComments
from .models import CourseResource


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")

        # 热门课程推荐
        hot_courses = Course.objects.all().order_by("-click_nums")[:3]

        # 课程排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            if sort == "hot":
                all_courses = all_courses.order_by("-click_nums")

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_courses, 2, request=request)

        courses = p.page(page)
        return render(request, 'course-list.html', {
            # 'all_courses': all_courses,  不分页时
            'all_courses': courses,  # 分页时
            'sort': sort,
            'hot_courses': hot_courses,
        })


class CourseDetailView(View):
    """
    课程详情页
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        # 增加课程点击数
        course.click_nums += 1
        course.save()

        # 激活章节、评论不同标签
        sort = request.GET.get('sort', '')

        has_fav_course = False
        has_fav_org = False

        # if request.user.is_authenticated():
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
        #         has_fav_course = True
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
        #         has_fav_org = True

        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            relate_courses = []
        return render(request, 'course-detail.html', {
            "course": course,
            "relate_courses": relate_courses,
            "sort": sort,
            # "has_fav_course": has_fav_course,
            # "has_fav_org": has_fav_org,
        })


class CourseInfoView(View):
    """
    课程章节信息
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_resources = CourseResource.objects.filter(course=course)
        # 激活章节、评论不同标签
        sort = request.GET.get('sort', '')

        return render(request, "course-video.html", {
            "course": course,
            "course_resources": all_resources,
            "sort": sort,
        })


class CommentsView(View):
    """
    课程评论
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        # 激活章节、评论不同标签
        sort = request.GET.get('sort', '')
        all_resources = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.filter(course=course)
        all_comments = all_comments.order_by("-add_time")

        return render(request, "course-comment.html", {
            "course": course,
            "course_resources": all_resources,
            "all_comments": all_comments,
            "sort": sort,
        })


class AddCommentView(View):
    """
    用户添加课程评论
    """
    def post(self, request):
        # 判断登陆状态
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail", "msg":"用户未登陆"}', content_type='application/json')

        course_id = request.POST.get("course_id", 0)
        comments = request.POST.get("comments", "")
        if course_id > str(0) and comments is not None:
            course_comments = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加失败"}', content_type='application/json')


