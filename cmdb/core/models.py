from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class TechnicalGroups(models.Model):
    """
    Technikai csoportok amelyekbe minden felhasznalo tartozik
    """

    name = models.CharField(unique=True, max_length=50)

    class Meta:
        ordering = ["name"]
        verbose_name = "Technical Group"
        verbose_name_plural = "Technical Groups"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class ManagementGroups(models.Model):
    """
    Management csoportok amelyekbe minden Manager tartozik
    """

    name = models.CharField(unique=True, max_length=50)

    class Meta:
        ordering = ["name"]
        verbose_name = "Management Group"
        verbose_name_plural = "Management Groups"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class UserProfile(AbstractUser):

    primary_tech_group = models.ForeignKey(TechnicalGroups, null=True, related_name="primary_members")
    secondary_tech_groups = models.ManyToManyField(TechnicalGroups, related_name="secondary_members")
    phone_number = models.CharField(max_length=15, null=True)

    def __str__(self):
        return "%s - %s" % (self.username, self.get_full_name())

    def __unicode__(self):
        return "%s - %s" % (self.username, self.get_full_name())


class ManagerProfile(UserProfile):
    approve_group = models.ManyToManyField(ManagementGroups, related_name="managing_members")

    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"
