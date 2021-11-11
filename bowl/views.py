from django.shortcuts import render, get_object_or_404
from .models import Locker


def index(request):
    """
    locker 목록 출력
    """
    locker_list = Locker.objects.order_by('-create_date')
    context = {'locker_list': locker_list}
    return render(request, 'bowl/locker_list.html', context)



def detail(request, locker_id):
    """
    locker 내용 출력
    """
    locker = get_object_or_404(Locker, pk=locker_id)
    context = {'locker': locker}
    return render(request, 'bowl/locker_detail.html', context)