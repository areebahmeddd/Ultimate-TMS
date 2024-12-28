from django.urls import path
from .views import TaskCreateView, TaskListView, TaskDetailView

urlpatterns = [
    path('task/create', TaskCreateView.as_view(), name='create_task'),
    path('task', TaskListView.as_view(), name='get_all_task'),
    path('task/<int:id>', TaskDetailView.as_view(), name='get_single_task'),
    path('task/<int:id>/update', TaskDetailView.as_view(), name='update_task'),
    path('task/<int:id>/delete', TaskDetailView.as_view(), name='delete_task'),
]
