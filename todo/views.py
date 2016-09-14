from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import TodoItem, TodoRevisions

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


