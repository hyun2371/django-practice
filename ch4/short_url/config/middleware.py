from django.conf import settings

class HiddenMethodOverrideMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method =="POST" and "_method" in request.POST: # requestbody안에 _method값 있으면
            override_method = request.POST["_method"]
            if override_method in ["PUT", "PATCH", "DELETE"]:
                request.method = override_method
                request.META["REQUEST_METHOD"] = override_method
                csrf_token = request.COOKIES.get(settings.CSRF_COOKIE_NAME)
                request.META[settings.CSRF_HEADER_NAME] = csrf_token
        return self.get_response(request)

"""
[브라우저]
POST /uK2SIxgb/
_method=DELETE
csrf=xxx
   ↓
[미들웨어]
POST → DELETE로 변경
CSRF 헤더 주입
   ↓
[View]
delete(request, code) 실행
"""