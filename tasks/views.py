from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.project = form.cleaned_data["project"]
            task.assignee = request.user
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)
