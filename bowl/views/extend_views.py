from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import datetime
from django.utils import timezone

from ..models import Locker
from django.db.models import F
from django.db import models


@login_required(login_url='common:login')
def extend_locker(request, locker_id):
    """
    locker 1년 연장
    """
    locker = get_object_or_404(Locker, pk=locker_id)
    if request.user.is_superuser:
        #만료일자를 유효일자로 변경 후 저장
        locker.effective_date = locker.expiration_date
        locker.save()

        #만료일자에 1년 추가 후 저장
        locker.expiration_date = locker.expiration_date + relativedelta(years=1)
        locker.modify_date = timezone.now()
        locker.save()

    else:
        messages.error(request, '관리자만 연장할 수 있습니다.')
    return redirect('bowl:detail', locker_id=locker.id)



@login_required(login_url='common:login')
def extend2_locker(request, locker_id):
    """
    locker 2년 연장
    """
    locker = get_object_or_404(Locker, pk=locker_id)
    if request.user.is_superuser:
        #만료일자를 유효일자로 변경 후 저장
        locker.effective_date = locker.expiration_date
        locker.save()

        #만료일자에 2년 추가 후 저장
        locker.expiration_date = locker.expiration_date + relativedelta(years=2)
        locker.modify_date = timezone.now()
        locker.save()

    else:
        messages.error(request, '관리자만 연장할 수 있습니다.')
    return redirect('bowl:detail', locker_id=locker.id)


@login_required(login_url='common:login')
def extend3_locker(request, locker_id):
    """
    locker 3년 연장
    """
    locker = get_object_or_404(Locker, pk=locker_id)
    if request.user.is_superuser:
        #만료일자를 유효일자로 변경 후 저장
        locker.effective_date = locker.expiration_date
        locker.save()

        #만료일자에 3년 추가 후 저장
        locker.expiration_date = locker.expiration_date + relativedelta(years=3)
        locker.modify_date = timezone.now()
        locker.save()

    else:
        messages.error(request, '관리자만 연장할 수 있습니다.')
    return redirect('bowl:detail', locker_id=locker.id)

