from django.db import models
from django.utils import timezone


class TodoRevisions(models.Model):
    crev = models.IntegerField(default=0)

    def new_revision(self, name, des, due_date):
        to = self.todoitem_set.create(name=name, des=des, date_created=timezone.now(), due_date=due_date)
        self.crev = to.id
        self.save()

    def get_current_revision(self):
        return self.todoitem_set.get(id=self.crev)

    def __str__(self):
        return self.crev.__str__()


class TodoItem(models.Model):
    history = models.ForeignKey(TodoRevisions, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200) #name of todo item
    des = models.CharField(max_length=500) #description of todo item
    date_created = models.DateTimeField('Date Created', null=True)
    due_date = models.DateTimeField('ToDo date', null=True)

    def __str__(self):
        return self.name



#from todo.models import TodoRevisions, TodoItem
#from django.utils import timezone
#.new_revision("test", "test", timezone.now())