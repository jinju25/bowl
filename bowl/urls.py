from django.urls import path

from .views import
app_name = 'bowl'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:locker_id>/', views.detail, name='detail'),
]