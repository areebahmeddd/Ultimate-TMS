from django.urls import path
from . import views

urlpatterns = [
    path('task/create', views.create_task, name='create_task'),
    path('task', views.get_all_task, name='get_all_task'),
    path('task/<int:id>', views.get_single_task, name='get_single_task'),
    path('task/<int:id>/update', views.update_task, name='update_task'),
    path('task/<int:id>/delete', views.delete_task, name='delete_task'),
]
