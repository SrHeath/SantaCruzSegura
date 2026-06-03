import threading

_thread_locals = threading.local()

def get_current_request():
    return getattr(_thread_locals, 'request', None)

def get_client_ip(request=None):
    if request is None:
        request = get_current_request()
    if request is None:
        return '127.0.0.1'
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
    return ip

class ThreadLocalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.request = request
        response = self.get_response(request)
        if hasattr(_thread_locals, 'request'):
            del _thread_locals.request
        return response


class CSPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Content-Security-Policy'] = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' 'unsafe-eval' cdn.jsdelivr.net unpkg.com; "
            "style-src 'self' 'unsafe-inline' cdn.jsdelivr.net unpkg.com fonts.googleapis.com fonts.gstatic.com; "
            "font-src 'self' cdn.jsdelivr.net fonts.gstatic.com fonts.googleapis.com; "
            "img-src 'self' data: mt1.google.com; "
            "connect-src 'self'; "
            "frame-src 'none'; "
            "base-uri 'self'; "
            "form-action 'self'"
        )
        return response
