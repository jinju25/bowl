from django.urls import path
from .views import base_views, extend_views, delete_views

app_name = 'bowl'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:locker_id>/', base_views.detail, name='detail'),

    # extend_views.py
    path('extend/locker/<int:locker_id>/', extend_views.extend_locker, name='extend_locker'),

    # extend_views.py
    path('extend2/locker/<int:locker_id>/', extend_views.extend2_locker, name='extend2_locker'),

    # extend_views.py
    path('extend3/locker/<int:locker_id>/', extend_views.extend3_locker, name='extend3_locker'),

    # extend_views.py
    path('delete/locker/<int:locker_id>/', delete_views.delete_locker, name='delete_locker'),


]