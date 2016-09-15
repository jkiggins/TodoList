from django.db import models
from django.utils import timezone


class TodoRevisions(models.Model):
    crev = models.IntegerField(default=0)

    def new_revision(self, status, des, due_date):
        to = self.todoitem_set.create(status=status, des=des, date_created=timezone.now(), due_date=due_date)
        self.crev = to.id
        self.save()

    def get_current_revision(self):
        return self.todoitem_set.get(id=self.crev)

    def get_current_revision_as_set(self):
        return self.todoitem_set.filter(id=self.crev)

    def __str__(self):
        return self.crev.__str__()


class TodoItem(models.Model):
    history = models.ForeignKey(TodoRevisions, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=200) #status of todo item
    des = models.CharField(max_length=500) #description of todo item
    date_created = models.DateTimeField('Date Created', null=True)
    due_date = models.DateTimeField('ToDo date', null=True)

    def __str__(self):
        return self.status



#from todo.models import TodoRevisions, TodoItem
#from django.utils import timezone
#.new_revision("test", "test", timezone.now())