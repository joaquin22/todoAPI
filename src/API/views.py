from rest_framework.viewsets import ModelViewSet

from API.models import Task
from API.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
