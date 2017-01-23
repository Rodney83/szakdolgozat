from cmdb.prototypes import viewsets
import models
import serializers


class ChangeRootView(viewsets.RootView):
    url_list = {
        'Changes': 'change-list',
        'Change States': 'changestate-list',
        'Tasks': 'task-list',
        'Task statuses': 'taskstatus-list',
        'Closure Codes': 'closurecode-list',
    }


class ChangeViewSet(viewsets.ModelViewSet):
    queryset = models.Change.objects.all()
    serializer_class = serializers.ChangeDetailSerializer
    serializer_map = {
        'list': serializers.ChangeListSerializer
    }


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskDetailSerializer
    serializer_map = {
        'list': serializers.TaskListSerializer
    }


class TaskStatusViewSet(viewsets.ModelViewSet):
    queryset = models.TaskStatus.objects.all()
    serializer_class = serializers.TaskStatusSerializer


class ChangeStateViewSet(viewsets.ModelViewSet):
    queryset = models.ChangeState.objects.all()
    serializer_class = serializers.ChangeStateSerializer


class ClosureCodeViewSet(viewsets.ModelViewSet):
    queryset = models.ClosureCode.objects.all()
    serializer_class = serializers.ClosureCodeSerializer
