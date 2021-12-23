from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *
from ..models import Locker
from django.db.models import F
from django.db import models


@login_required(login_url='common:login')
def extend_locker(request, locker_id):
    """
    locker 연장하기 !!!
    """
    locker = get_object_or_404(Locker, pk=locker_id)
    if request.user.is_superuser:
        Locker.expiration_date + datetime.timedelta(years=1)
        Locker.save()
    else:
        messages.error(request, '관리자만 연장할 수 있습니다.')
    return redirect('bowl:detail', locker_id=locker.id)