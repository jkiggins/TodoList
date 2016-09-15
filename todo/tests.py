from django.test import TestCase
from .models import TodoRevisions, TodoItem
from django.utils import timezone

class test_TodoRevision_ability(TestCase):

    def test_todo_revision_by_adding_new_revisions(self):
        tdr = TodoRevisions.objects.create()
        tdr.new_revision("test", "test", timezone.now())
        tdr.save()

        to = tdr.todoitem_set.get(id=1)

        self.assertEqual(tdr.crev, 1)
        self.assertEqual(to.status, "test")

        tdr.new_revision("test1", "test1", timezone.now())
        tdr.save()

        self.assertEqual(tdr.crev, 2)
        self.assertEqual(tdr.get_current_revision().status, "test1")

