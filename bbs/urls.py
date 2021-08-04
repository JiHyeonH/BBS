from django.urls import path
from . import views

app_name = 'bbs'    # namespace를 bbs로 지정
# http://localhost:8000/bbs/

urlpatterns = [
    path('list/', views.b_list, name='b_list'),
    path('create/', views.b_create, name='b_create'),
    path('<int:post_id>/detail/', views.b_detail, name='b_detail'),
    path('<int:post_id>/fix/', views.b_fix, name='b_fix')
]
