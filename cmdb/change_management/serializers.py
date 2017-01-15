from rest_framework import serializers
import models
import core.serializers


class AffectedCiSerializer(serializers.ModelSerializer):
    affected_ci = serializers.SlugRelatedField(slug_field='logical_name', queryset=models.ConfigurationItem)
    affected_ci_verbose = serializers.SlugRelatedField(source='affected_ci', slug_field='verbose_name',
                                                    queryset=models.ConfigurationItem)
    affected_ci_url = serializers.HyperlinkedRelatedField(source='affected_ci', view_name='configurationitem-detail',
                                                          read_only=True)

    class Meta:
        model = models.Task
        fields = ('affected_ci', 'affected_ci_verbose', 'affected_ci_url')


class TaskListSerializer(serializers.HyperlinkedModelSerializer, AffectedCiSerializer):
    parent_change = serializers.SlugRelatedField(slug_field='changeid', source='change', read_only=True)
    parent_change_url = serializers.HyperlinkedRelatedField(source='change', view_name='change-detail', read_only=True)
    taskid = serializers.CharField(read_only=True)
    status = serializers.SlugRelatedField(slug_field='name', queryset=models.TaskStatus.objects.all())
    closure_code = serializers.SlugRelatedField(slug_field='name', queryset=models.ClosureCode.objects.all())
    technical_assignment = serializers.SlugRelatedField(slug_field='name',
                                                        queryset=models.TechnicalGroups.objects.all())

    class Meta:
        model = models.Task
        fields = AffectedCiSerializer.Meta.fields + (
            'url',
            'parent_change',
            'parent_change_url',
            'taskid',
            'title',
            'status',
            'affected_ci',
            'affected_ci_url',
            'closure_code',
            'planned_start',
            'planned_end',
            'technical_assignment',
        )


class TaskDetailSerializer(TaskListSerializer):
    open_time = serializers.DateTimeField(read_only=True)
    executor = core.serializers.UserProfileMinimalSerializer(read_only=True)
    approval_group = serializers.SlugRelatedField(slug_field='name', queryset=models.TechnicalGroups.objects.all())
    technical_approver = core.serializers.UserProfileMinimalSerializer(read_only=True)
    close_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = TaskListSerializer.Meta.model
        fields = TaskListSerializer.Meta.fields + (
            'close_time',
            'open_time',
            'description',
            'fallback',
            'executor',
            'approval_group',
            'technical_approval',
            'technical_approver',
        )


class ChangeListSerializer(serializers.HyperlinkedModelSerializer):
    changeid = serializers.CharField(read_only=True)
    state = serializers.SlugRelatedField(slug_field='name', queryset=models.ChangeState.objects.all())
    closure_code = serializers.SlugRelatedField(slug_field='name', queryset=models.ClosureCode.objects.all())
    owner_assignment = serializers.SlugRelatedField(slug_field='name', queryset=models.TechnicalGroups.objects.all())

    class Meta:
        model = models.Change
        fields = (
            'url',
            'changeid',
            'title',
            'state',
            'closure_code',
            'planned_start',
            'planned_end',
            'owner_assignment',
        )


class ChangeDetailSerializer(ChangeListSerializer):
    close_time = serializers.DateTimeField(read_only=True)

    open_time = serializers.DateTimeField(read_only=True)
    owner = core.serializers.UserProfileMinimalSerializer(read_only=True)
    approval_group = serializers.SlugRelatedField(slug_field='name', queryset=models.ManagementGroups.objects.all())
    management_approver = core.serializers.ManagerProfileMinimalSerializer(read_only=True)
    tasks = TaskListSerializer(read_only=True, many=True)
    affected_cis = AffectedCiSerializer(source='tasks', many=True, read_only=True)

    class Meta:
        model = ChangeListSerializer.Meta.model
        fields = ChangeListSerializer.Meta.fields + (
            'close_time',
            'open_time',
            'description',
            'reason',
            'owner',
            'approval_group',
            'management_approval',
            'management_approver',
            'tasks',
            'affected_cis',
        )


class TaskStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TaskStatus
        fields = ('id', 'name')


class ChangeStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChangeState
        fields = ('id', 'name')


class ClosureCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChangeState
        fields = ('id', 'name')
