# _*_coding_*_ utf-8
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

__date__ = '2017/8/1 9:31'


class LoginRequiredMixin(object):
    
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

