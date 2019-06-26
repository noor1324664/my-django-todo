from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .models import List

# THIS IS THE MAIN SPLASH SCREEN FOR THE WEBSITE
def splash(request):
    return render(request, 'todo_app/splash.html')


# THESE HANDLE THE UI BEFORE THE USER HAS SELECTED WHICH LIST THEY WANT TO WORK ON
@login_required
def lists(request):
    # GET ALL LISTS
    user = request.user
    user_id = user.id
    lists = List.objects.filter(user_id = user_id)

    # CREATE A CONTAINER FOR THE LIST AND THE NUMBER OF TASKS IN THAT LIST
    num_lists = []

    for list in lists:
        num_tasks = Task.objects.filter(list_id = list.id).count()
        num_lists.append({"list": list, "num_tasks": num_tasks})

    # RENDER THE SCREEN
    context = {'user': user, 'num_lists': num_lists}
    return render(request, 'todo_app/lists.html', context)

@login_required
def createlist(request):
    if request.method == 'GET':
        # IF GET, RENDER THE SCREEN
        context = {}
        return render(request, 'todo_app/createlist.html', context)
    elif request.method == 'POST':
        # IF POST, CREATE A NEW TASK ITEM AND SAVE TO DATABASE
        name = request.POST.get('name')
        if len(name) > 200:
            name = name[0:200:]
        user_id = request.user.id
        list = List(name = name, user_id = user_id)
        list.save()
        # REDIRECT TO THE MAIN PAGE
        return redirect('/todo')


@login_required
def deletelist(request, list):
    if request.method == 'GET':
        user_id = request.user.id
        num_tasks = Task.objects.filter(list_id = list, user_id = user_id).count()
        if num_tasks == 0:
            return redirect(f'/todo/deletelistconfirm/{list}')
        context = {'list': list, 'num_tasks': num_tasks}
        return render(request, 'todo_app/deletelist.html', context)


@login_required
def deletelistconfirm(request, list):
    if request.method == 'GET':
        user_id = request.user.id
        Task.objects.filter(list_id = list, user_id = user_id).delete()
        List.objects.filter(id = list, user_id = user_id).delete()
        return redirect('/todo')


# THESE HANDLE UI FOR A USER ONCE THEY HAVE SIGNED IN AND SELECTED A LIST
@login_required
def index(request, list):
    # GET ALL TASK ITEMS
    user = request.user
    user_id = user.id
    tasks = Task.objects.filter(user_id = user_id, list_id = list)

    # RENDER THE SCREEN
    context = {'tasks': tasks, 'user': user, 'list': list}
    return render(request, 'todo_app/index.html', context)


@login_required
def details(request, list, id):
    # GET THE TASK ITEM
    user_id = request.user.id
    task = Task.objects.get(id=id, user_id = user_id)

    if request.method == 'GET':
        # RENDER THE SCREEN
        context = {'task': task, 'list': list}
        return render(request, 'todo_app/details.html', context)
    

@login_required
def edit(request, list, id):
    # GET THE TASK ITEM
    user_id = request.user.id
    task = Task.objects.get(id=id, user_id = user_id)

    if request.method == 'GET':
        # IF GET, RENDER THE SCREEN
        context = {'task': task, 'list': list}
        return render(request, 'todo_app/edit.html', context)
    elif request.method == 'POST':
        # IF POST, UPDATE THE TASK AND REDIRECT TO THE MAIN SCREEN
        task.name = request.POST.get('name')
        task.description = request.POST.get('description')
        task.save()
        return redirect(f'/todo/tasks/{list}')


@login_required
def create(request, list):
    if request.method == 'GET':
        # IF GET, RENDER THE SCREEN
        context = {'list': list}
        return render(request, 'todo_app/create.html', context)
    elif request.method == 'POST':
        # IF POST, CREATE A NEW TASK ITEM AND SAVE TO DATABASE
        name = request.POST.get('name')
        if len(name) > 200:
            name = name[0:200:]
        description = request.POST.get('description')
        user_id = request.user.id
        task = Task(name = name, description = description, user_id = user_id, list_id = list)
        task.save()
        # REDIRECT TO THE MAIN PAGE
        return redirect(f'/todo/tasks/{list}')


@login_required
def delete(request, list, id):
    if request.method == 'GET':
        # IF GET, DELETE THE ITEM REQUESTED
        user_id = request.user.id
        task = Task.objects.filter(id=id, user_id = user_id).delete()
        return redirect(f'/todo/tasks/{list}')


@login_required
def check(request, list, id):
    if request.method == 'GET':
        user_id = request.user.id
        task = Task.objects.get(id=id, user_id = user_id)
        if task.is_done:
            task.is_done = False
        else:
            task.is_done = True
        task.save()
    return redirect(f'/todo/tasks/{list}')
