from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages 
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def helloworld(request):
    return HttpResponse('Hello World!')
@login_required
def taskList(request):
    search = request.GET.get('search')

    if search:
        tasks = Task.objects.filter(title__icontains=search)
    else:
        tasks = Task.objects.all().order_by('-created_at')#Ele é usado para ordenar um conjunto de dados por data de criação, em ordem decrescente.
        paginator = Paginator(tasks, 3)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
        

    return render(request, 'list.html', {'tasks': tasks})    
@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'task.html', {'task': task})

@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
            
    else:
        form = TaskForm()
        return render(request, 'addtask.html', {'form': form})
    
@login_required    
def yourName(request, name):
    return render(request, 'yourname.html', {'name': name})

@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'edittask.html', {'form': form, 'task': task})
    
@login_required    
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('/')