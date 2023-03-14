from django.shortcuts import render, redirect

tasks = ["foo", "bar", "baz"]

# Create your views here.

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    if request.method == 'POST':
        task = request.POST.get('task')

        tasks.append(task)
        return  redirect('tasks:index')

    return render(request, "tasks/add.html")