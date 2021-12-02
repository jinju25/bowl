from django.shortcuts import render, get_object_or_404
from .models import Locker
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages


def index(request):
    """
    locker 목록 출력
    """

    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    locker_list = Locker.objects.order_by()
    if kw:
        locker_list = locker_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(name__icontains=kw) |  # 이름검색
            Q(club__icontains=kw)   # 클럽럽검색
       ).distinct()

    # 페이징처리
    paginator = Paginator(locker_list, 5)  # 페이지당 1000개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'locker_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'bowl/locker_list.html', context)




def detail(request, locker_id):
    """
    locker 내용 출력
    """
    locker = get_object_or_404(Locker, pk=locker_id)
    context = {'locker': locker}
    return render(request, 'bowl/locker_detail.html', context)


