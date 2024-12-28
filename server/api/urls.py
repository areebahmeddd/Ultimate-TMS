from django.urls import path
from . import views

urlpatterns = [
    path('task/create', views.create_task, name='create_task'),
]
