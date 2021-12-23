from django.urls import path
from .views import base_views, extend_views

app_name = 'bowl'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:locker_id>/', base_views.detail, name='detail'),
    path('locker/extend/<int:locker_id>/', base_views.locker_extend, name='locker_extend'),

    # extend_views.py
    path('extend/locker/<int:locker_id>/', extend_views.extend_locker, name='extend_locker'),
]