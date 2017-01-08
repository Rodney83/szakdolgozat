from __future__ import unicode_literals

from django.db import models
from core import abstract_models
from core.models import UserProfile, ManagerProfile, TechnicalGroups, ManagementGroups


class TaskStatus(abstract_models.ActiveFieldModelAbstract):
    name = models.CharField(max_length=50)


class ChangeState(abstract_models.ActiveFieldModelAbstract):
    name = models.CharField(max_length=50)


class ClosureCode(abstract_models.ActiveFieldModelAbstract):
    name = models.CharField(max_length=50)


class Change(models.Model):
    changeid = models.CharField(max_length=45, unique=True)
    title = models.CharField(max_length=255)
    state = models.ForeignKey(ChangeState)
    close_time = models.DateTimeField(null=True)
    closure_code = models.CharField(max_length=255, null=True)
    open_time = models.DateTimeField(auto_now_add=True)
    planned_start = models.DateTimeField(auto_now_add=True)
    planned_end = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000)
    reason = models.TextField(max_length=500, null=True)
    owner_assignment = models.ForeignKey(TechnicalGroups, related_name="owned_changes")
    owner = models.ForeignKey(UserProfile, related_name="assigned_changes")
    approval_group = models.ForeignKey(ManagementGroups, null=True)
    management_approval = models.NullBooleanField(default=None)
    management_approver = models.ForeignKey(ManagerProfile, null=True)


class Task(models.Model):
    change = models.ForeignKey(Change)
    taskid = models.CharField(max_length=45, unique=True)
    title = models.CharField(max_length=255)
    status = models.ForeignKey(TaskStatus)
    close_time = models.DateTimeField(null=True)
    closure_code = models.CharField(max_length=255, null=True)
    open_time = models.DateTimeField(auto_now_add=True)
    planned_start = models.DateTimeField(auto_now_add=True)
    planned_end = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000)
    fallback = models.TextField(max_length=500, null=True)
    technical_assignment = models.ForeignKey(TechnicalGroups, related_name="assigned_tasks")
    executor = models.ForeignKey(UserProfile, related_name="assigned_tasks")
    approval_group = models.ForeignKey(TechnicalGroups, null=True)
    technical_approval = models.NullBooleanField(default=None)
    technical_approver = models.ForeignKey(UserProfile, null=True)
