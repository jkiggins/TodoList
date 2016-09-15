from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import TodoItem, TodoRevisions
from django.utils import timezone
from django.utils.dateparse import parse_datetime


def index(request, order):

    revs = TodoRevisions.objects.all().order_by('-crev')
    ret = TodoItem.objects.all().filter(id=-1)

    for r in revs:
        ret |= r.get_current_revision_as_set()

    order_map = {'obstat': 'status', 'obdes': 'des', 'obdc': 'date_created', 'obdd': 'due_date'}

    context = {'current_todos': ret}

    obstr = ''
    if order != '':
        if order[0] == 'r':
            obstr='-'
            order = order[1:]

        if order in order_map.keys():
            obstr += order_map[order]
            context = {'current_todos': ret.order_by(obstr)}

    return render(request, 'todo/index.html', context)


def detail(request, pk):
    tdi = get_object_or_404(TodoItem, pk=pk)

    dt_html_str = '{0}-{1:02d}-{2:02d}T{3:02d}:{4:02d}'.format(tdi.due_date.year, tdi.due_date.month, tdi.due_date.day, tdi.due_date.hour, tdi.due_date.minute)

    context = {'todoitem': tdi, 'past_revs': tdi.history.todoitem_set.all().order_by('-date_created'), 'html5date': dt_html_str}

    return render(request, 'todo/detail.html', context)


def newtodo(request):
    tdr = TodoRevisions()
    tdr.save()
    tdr.new_revision(request.POST['status'], request.POST['des'], parse_datetime(request.POST['due_date']))
    tdr.save()


    return HttpResponseRedirect(reverse('todo:index', kwargs={'order': ''}))

def edittodo(request, pk):
    tdi = get_object_or_404(TodoItem, pk=pk)
    tdr = tdi.history

    if request.POST['status'] != '' and request.POST['des'] != '' and request.POST['due_date'] != '':

        match = TodoItem.objects.all().exists

        if match != 0:

            tdr.new_revision(request.POST['status'], request.POST['des'], parse_datetime(request.POST['due_date']))
            tdr.save()

    return HttpResponseRedirect(reverse('todo:index', kwargs={'order': ''}))

def delete(request, pk):
    tdr = get_object_or_404(TodoRevisions, crev=pk)
    tdr.delete()

    return HttpResponseRedirect(reverse('todo:index', kwargs={'order': ''}))