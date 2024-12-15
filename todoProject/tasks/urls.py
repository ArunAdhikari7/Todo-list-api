from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.create_task, name='create_task'),
    path('tasks/all/', views.get_all_tasks, name='get_all_tasks'),
    path('tasks/<int:pk>/', views.get_task, name='get_task'),
    path('tasks/update/<int:pk>/', views.update_task, name='update_task'),
    path('tasks/delete/<int:pk>/', views.delete_task, name='delete_task'),
]
