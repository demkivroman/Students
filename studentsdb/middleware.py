from datetime import datetime
from django.http import HttpResponse

class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        request.start_time = datetime.now()

        response = self.get_response(request)

        if not hasattr(request, 'start_time'):
            return response

        # canculate request execution time
        request.end_time = datetime.now()
        if __debug__:
            if 'text/html' in response.get('Content-Type',''):
                response.write('<br />Request took: %s' % str(request.end_time - request.start_time))

        return response

    def process_view(self, request, view, args, kwargs):
        return None

    def process_template_response(self, request, response):
        return response

    def process_exception(self, request, exception):
        return HttpResponse('Exception found: %s' % exception)

















