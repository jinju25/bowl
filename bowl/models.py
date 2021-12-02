from django.db import models
from datetime import date



class Locker(models.Model):

    subject = models.CharField(max_length=4)  # 락커 번호
    size = models.CharField(max_length=1, null=True)  # 락커 size
    name = models.CharField(max_length=10, null=True, blank=True)  # 사용자 이름
    club = models.CharField(max_length=11, null=True, blank=True)  # 소속 클럽
    phone_number = models.CharField(max_length=20, null= True, blank=True)
    effective_date = models.DateField(null= True, blank=True) # 락커 유효일자 (계약이 시작되는 일자)
    expiration_date = models.DateField(null= True, blank=True)    # 락커 만료일자 (계약이 끝나는 일자)

    modify_date = models.DateTimeField(null=True, blank=True)  # 수정 일시

    objects = models.Manager()

    def __str__(self):
        return self.subject


    def is_past_due(self):
        return date.today() > self.expiration_date



