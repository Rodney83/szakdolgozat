from django.shortcuts import render
from cmdb.prototypes import viewsets
import models
import serializers


class ChangeListViewSet(viewsets.ListViewSet):
    queryset = models.Change.objects.all()
    serializer_class = serializers.ChangeListSerializer


class ChangeDetailViewSet(viewsets.CreateDestroyRetrieveUpdateViewSet):
    queryset = models.Change.objects.all()
    serializer_class = serializers.ChangeDetailSerializer


class TaskListViewSet(viewsets.ListViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskListSerializer


class TaskDetailViewset(viewsets.CreateDestroyRetrieveUpdateViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskDetailSerializer


class TaskStatusViewSet(viewsets.ListViewSet):
    queryset = models.TaskStatus.objects.all()
    serializer_class = serializers.TaskStatusSerializer


class ChangeStateViewSet(viewsets.ListViewSet):
    queryset = models.ChangeState.objects.all()
    serializer_class = serializers.ChangeStateSerializer


class ClosureCodeViewSet(viewsets.ListViewSet):
    queryset = models.ClosureCode.objects.all()
    serializer_class = serializers.ClosureCodeSerializer