from typing import Any
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from .models import TaskList
# Create your views here.
class ListForm(CreateView):
    model = TaskList
    fields = ['title', 'description']
    template_name = 'first_app/home.html'
    success_url = '/show_list/'

class ShowList(ListView):
    model = TaskList
    template_name = 'first_app/show.html'
    context_object_name = 'items'
    
class ModifyView(UpdateView):
    model = TaskList
    fields = ['title', 'description']
    template_name = 'first_app/home.html'
    success_url = '/show_list/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = 'modify'
        return context
        
def delete_field(request, id):
    field = TaskList.objects.get(pk=id).delete()
    return redirect('show')


def status_modify(request, id):
    task_list = TaskList.objects.get(pk = id)
    task_list.status = 'Complete'
    task_list.save()
    return redirect('show')
    