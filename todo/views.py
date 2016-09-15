from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from .models import TodoItem, TodoRevisions
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.db.models.query import QuerySet

class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'current_todos'

    def get_queryset(self):
        '''return the most recent question from each TodoRevisions entry'''
        revs = TodoRevisions.objects.all().order_by('-crev')
        ret = []

        for r in revs:
            ret.append(r.get_current_revision())

        return ret

def detail(request, pk):
    tdi = get_object_or_404(TodoItem, pk=pk)

    context = {'todoitem': tdi, 'past_revs': tdi.history.todoitem_set.all().order_by('date_created')}

    return render(request, 'todo/detail.html', context)


def newtodo(request):
    tdr = TodoRevisions()
    tdr.save()
    tdr.new_revision(request.POST['name'], request.POST['des'], parse_date(request.POST['due_date']))
    tdr.save()


    return HttpResponseRedirect(reverse('todo:index'))

def edittodo(request, pk):
    tdi = get_object_or_404(TodoItem, pk=pk)
    tdr = tdi.history

    if request.POST['name'] != '' and request.POST['des'] != '' and request.POST['due_date'] != '':

        date = parse_date(request.POST['due_date'])
        match = TodoItem.objects.all().exists

        if match != 0:

            tdr.new_revision(request.POST['name'], request.POST['des'], parse_date(request.POST['due_date']))
            tdr.save()

    return HttpResponseRedirect(reverse('todo:index'))