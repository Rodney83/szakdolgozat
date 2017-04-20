from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class LoggedInRedirect(MiddlewareMixin):
    """
    Redirect the user if loggegd in. Redirect to login if not authenticated.
    """

    def process_request(self, request):

        if request.user.is_authenticated():
            if request.get_full_path().startswith('/login/'):
                return HttpResponseRedirect('/')
        else:
            if request.get_full_path() != '/login/':
                return HttpResponseRedirect('/login/')
