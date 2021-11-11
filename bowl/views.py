from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요 성암볼링장입니다.")