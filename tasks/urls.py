from django.urls import path
from .views import helloworld, taskList, yourName, taskView, newTask, editTask, deleteTask

urlpatterns = [
    path('helloworld/', helloworld),
    path('', taskList, name='task-list'),
    path('task/<int:id>', taskView, name='task-view'),
    path('newtask/',newTask, name='new-task'),
    path('yourname/<str:name>/', yourName, name='your-name'),
    path('edit/<int:id>/', editTask, name='edit-task'),
    path('delete/<int:id>/', deleteTask, name='delete-task'),
]