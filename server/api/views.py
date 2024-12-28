from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Task
import json

@method_decorator(csrf_exempt, name='dispatch')
class TaskCreateView(View):
    def post(self, request):
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

class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return JsonResponse(list(tasks.values()), safe=False)

class TaskDetailView(View):
    def get(self, request, id):
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

    @method_decorator(csrf_exempt)
    def put(self, request, id):
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
        return JsonResponse({'message': 'Task updated successfully!'}, status=200)

    @method_decorator(csrf_exempt)
    def delete(self, request, id):
        task = Task.objects.get(id=id)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully!'}, status=204)
