from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json

@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task = Task.objects.create(
            title=data['title'],
            description=data['description'],
            is_completed=data['is_completed'],
            due_date=data['due_date'],
            priority=data['priority']
        )

        return JsonResponse({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'is_completed': task.is_completed,
            'due_date': task.due_date,
            'priority': task.priority,
            'created_at': task.created_at,
            'updated_at': task.updated_at
        }, status=201)

@csrf_exempt
def get_all_task(request):
    if request.method == 'GET':
        task = Task.objects.all()
        return JsonResponse(list(task.values()), safe=False)

def get_single_task(request, id):
    if request.method == 'GET':
        task = Task.objects.get(id=id)
        return JsonResponse({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'is_completed': task.is_completed,
            'due_date': task.due_date,
            'priority': task.priority,
            'created_at': task.created_at,
            'updated_at': task.updated_at
        })
