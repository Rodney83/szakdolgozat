from __future__ import unicode_literals

from django.db import models
from core.models import UserProfile, TechnicalGroups


class ConfigurationItem(models.Model):
    """
    Az konfiguracios elemek mind osztoznak egy kozos reszen.
    Ezek vannak tarolva ebben a tablaban
    """

    # Graf bejarasahoz szukseges attributum
    traverse_mark = models.BooleanField(default=False)

    logical_name = models.CharField(max_length=20, db_index=True, unique=True)
    verbose_name = models.CharField(max_length=250, null=True)
    status = models.CharField(max_length=15, null=True)
    ci_type = models.CharField(max_length=3, null=True)
    last_mod_time = models.DateTimeField(auto_now_add=True, verbose_name="Last modification")
    engineering_group = models.ForeignKey(TechnicalGroups, related_name="ci_config_admin_group", null=True)
    administrator_groups = models.ManyToManyField(TechnicalGroups, related_name="ci_support_groups")
    responsible = models.ForeignKey(UserProfile, null=True, related_name="owned_system")