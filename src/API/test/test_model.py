import pytest

from API.models import Task

pytestmark = pytest.mark.django_db


class TestTask:
    def setup_method(self):
        self.task = Task.objects.create(
            title="Test Task", description="Test Description", completed=False
        )

    def test_task_creation(self, db):
        task = Task.objects.create(
            title="Test Task", description="Test Description", completed=False
        )
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed == False

    def test_task_update(self, db):
        self.task.title = "Update Title"
        self.task.description = "Update Description"
        self.task.completed = True
        self.task.save()
        assert self.task.title == "Update Title"
        assert self.task.description == "Update Description"
        assert self.task.completed == True

    def test_task_delete(self, db):
        self.task.delete()
        assert Task.objects.all().count() == 0
