from django.urls import path
from . import views

urlpatterns = [
    path('api/tasks/', views.TaskList.as_view(), name='task_list'),  # Task list URL
    path('', views.task_list_page, name='task-list-page'),
    path('create-task/', views.create_task, name='create_task'),
]