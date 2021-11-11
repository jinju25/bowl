from django.contrib import admin
from .models import Locker

class LockerAdmin(admin.ModelAdmin):
    search_fields = ['content']


admin.site.register(Locker, LockerAdmin)