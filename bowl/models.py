from django.db import models


class Locker(models.Model):

    size = models.CharField(max_length=200) # 락커 size
    number = models.CharField(max_length=200)  # 락커 number
    content = models.TextField()  # 락커 내용 (이름,클럽,전화번호)

    effective_date = models.DateTimeField() # 락커 유효일자 (계약이 시작되는 일자)
    expiration_date = models.DateTimeField()    # 락커 만료일자 (계약이 끝나는 일자)

    create_date = models.DateTimeField()  # 수정 일시
