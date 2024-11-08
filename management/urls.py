from django.urls import path
from . import views

urlpatterns = [
    path('sub/insert', views.insert_subject, name='insert_subject'),
    path('sub/list', views.list_subject, name='list_subject'),
    
    path('major/insert', views.insert_major, name='insert_major'),
    path('major/list', views.list_major, name='list_major'),
    path('major/edit', views.edit_major, name='edit_major'),

    
    path('student/insert', views.insert_student, name='insert_student'),

    
    path('', views.list, name='list')

]
