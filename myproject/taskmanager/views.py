from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Tasks
from .serializers import TasksSerializer

class TaskList(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()  # Queryset to retrieve all tasks
    serializer_class = TasksSerializer

def task_list_page(request):
    return render(request, 'tasks.html')

def create_task(request):
    if request.method == 'POST':
        # Get data from form submission
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        
        # Create a new task instance and save to the database
        task = Tasks(title=title, description=description, due_date=due_date, priority=priority)
        task.save()
        
        # Redirect to a success page or the task list after creation
        return redirect('task_list')  # Assuming you have a view that lists tasks

    return render(request, 'new_task.html')