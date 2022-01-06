from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from ..models import Locker



@login_required(login_url='common:login')
def delete_locker(request, locker_id):
    """
    locker 뺌
    """
    locker = get_object_or_404(Locker, pk=locker_id)
    if request.user.is_superuser:
        locker.name = None
        locker.phone_number = None
        locker.club = None
        locker.expiration_date = None
        locker.effective_date = None

        locker.save()


    else:
        messages.error(request, '관리자만 연장할 수 있습니다.')
    return redirect('bowl:detail', locker_id=locker.id)
