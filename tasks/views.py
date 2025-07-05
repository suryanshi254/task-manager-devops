from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.utils import timezone

# Show all tasks
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Add new task
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description, created_at=timezone.now())
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')

# Delete task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

