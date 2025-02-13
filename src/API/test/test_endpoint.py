import pytest
from model_bakery import baker

from API.models import Task

pytestmark = pytest.mark.django_db


class TestTaskEndpoint:
    def test_task_list(self, api_client):
        baker.make(Task, 5)
        response = api_client().get("/api/tasks/")
        assert response.status_code == 200
        assert len(response.json()) == 5

    def test_task_create(self, api_client):
        response = api_client().post(
            "/api/tasks/",
            data={
                "title": "Test Task",
                "description": "Test Description",
                "completed": False,
            },
        )
        assert response.status_code == 201
        assert response.json()["title"] == "Test Task"

    def test_task_update(self, api_client):
        task = baker.make(Task)
        response = api_client().put(
            f"/api/tasks/{task.id}/",
            data={
                "title": "Update Title",
                "description": "Update Description",
                "completed": True,
            },
        )
        assert response.status_code == 200
        assert response.json()["title"] == "Update Title"

    def test_task_delete(self, api_client):
        task = baker.make(Task)
        response = api_client().delete(f"/api/tasks/{task.id}/")
        assert response.status_code == 204
