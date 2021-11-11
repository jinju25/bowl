from django.urls import path

from . import views

app_name = 'bowl'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:locker_id>/', views.detail, name='detail'),
]