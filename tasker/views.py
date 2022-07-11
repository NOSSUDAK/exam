from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from tasker.models import Task, Tag


def toggle_task_status(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_done:
        task.is_done = False
    else:
        task.is_done = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("tasker:task-list"))


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasker/index.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasker:task-list")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasker:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasker:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasker:tag-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasker:tag-list")

class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasker:tag-list")
