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
        }, status=200)

@csrf_exempt
def update_task(request, id):
    if request.method == 'PUT':
        task = Task.objects.get(id=id)
        data = json.loads(request.body)

        if 'title' in data:
            task.title = data['title']
        if 'description' in data:
            task.description = data['description']
        if 'is_completed' in data:
            task.is_completed = data['is_completed']
        if 'due_date' in data:
            task.due_date = data['due_date']
        if 'priority' in data:
            task.priority = data['priority']

        task.save()
        return JsonResponse({'message': 'Task was updated successfully!'}, status=200)

@csrf_exempt
def delete_task(request, id):
    if request.method == 'DELETE':
        task = Task.objects.get(id=id)
        task.delete()

        return JsonResponse({'message': 'Task was deleted successfully!'}, status=204)
