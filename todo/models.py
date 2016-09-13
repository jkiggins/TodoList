from django.db import models


class TodoItem(models.Model):
    name = models.CharField(max_length=200) #name of todo item
    des = models.CharField(max_length=500) #description of todo item
    rev_id = models.CharField(max_length=200) #revision id, shared by all revisions
    rev_num = models.IntegerField(default=0)

