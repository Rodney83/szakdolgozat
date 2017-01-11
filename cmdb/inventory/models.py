from __future__ import unicode_literals

from django.db import models

from core import abstract_models
from core.models import UserProfile, ManagerProfile, TechnicalGroups, ManagementGroups


class CiStatus(abstract_models.ActiveFieldModelAbstract):
    """
    A konfiguracios elemek lehetseges statuszai
    """

    name = models.CharField(max_length=15, null=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Statusz"
        verbose_name_plural = "Statuszok"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class CiType(abstract_models.ActiveFieldModelAbstract):
    """
    Konfiguracios elem tipusok
    """

    name = models.CharField(max_length=15, null=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Tipus"
        verbose_name_plural = "Tipusok"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class ConfigurationItem(models.Model):
    """
    Az konfiguracios elemek mind osztoznak egy kozos reszen.
    Ezek vannak tarolva ebben a tablaban
    A graf pontjai
    """

    # Graf bejarasahoz szukseges attributum
    traverse_mark = models.BooleanField(default=False)

    logical_name = models.CharField(max_length=20, db_index=True, unique=True, help_text="Az elem logikai azonositoja")
    verbose_name = models.CharField(max_length=250, null=True, help_text="Az elem elnevezese")
    status = models.ForeignKey(CiStatus, related_name="with_status")
    ci_type = models.ForeignKey(CiType, related_name="with_type")
    last_mod_time = models.DateTimeField(auto_now_add=True, help_text="Utolso modositas datuma")
    engineering_group = models.ForeignKey(TechnicalGroups, related_name="engineered_systems", null=True,
                                          help_text="Mernoki csoport")
    administrator_groups = models.ManyToManyField(TechnicalGroups, related_name="administrated_systems",
                                                  help_text="Adminisztrator csoport")
    responsible = models.ForeignKey(UserProfile, null=True, related_name="owned_system")

    class Meta:
        default_permissions = ("view", "add", "change")
        ordering = ["verbose_name"]
        verbose_name = "Konfiguracios Elem"
        verbose_name_plural = "Konfiguracios Elemek"

    def __str__(self):
        return "%s (%s)" % (self.verbose_name, self.logical_name)

    def __unicode__(self):
        return "%s (%s)" % (self.verbose_name, self.logical_name)


class CiRelation(models.Model):
    """
    A konfiguracios elemek kozotti kapcsolatok.
    A graf elei
    """

    parent_ci = models.ForeignKey(ConfigurationItem, db_index=True, related_name="children")
    child_ci = models.ForeignKey(ConfigurationItem, db_index=True, related_name="parents")
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["parent_ci__verbose_name"]
        verbose_name = "Elem Kapcsolat"
        verbose_name_plural = "Elem Kapcsolatok"

    def __str__(self):
        return "%s -> %s" % (self.parent_ci, self.child_ci)

    def __unicode__(self):
        return "%s -> %s" % (self.parent_ci, self.child_ci)


class Vendors(abstract_models.ActiveFieldModelAbstract):
    """
    Hardware gyartok
    """

    name = models.CharField(max_length=15, null=True)
    contact_email = models.EmailField(max_length=15, null=True)
    contact_phone = models.CharField(max_length=15, null=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Gyarto"
        verbose_name_plural = "Gyartok"


class IpAddress(abstract_models.ActiveFieldModelAbstract):
    """
    Ip cimek es hozzatartozo fqdn-ek
    """
    ip = models.GenericIPAddressField()
    fqdn = models.CharField(max_length=50)


class CiNetworkNode(ConfigurationItem):
    hardware_vendor = models.ForeignKey(Vendors, related_name="network_nodes")
    number_of_ports = models.PositiveIntegerField(null=True)
    ip_addresses = models.ForeignKey(IpAddress)


class CiServerNode(ConfigurationItem):
    """
    ServerNode-okra vonatkoz specifikus adatok
    """
    console_address = models.ForeignKey(IpAddress)
    memory_size = models.PositiveIntegerField(null=True, help_text="Memory size in MB")
    cpu_cores = models.PositiveIntegerField(null=True, help_text="Number of CPU cores")
    description = models.TextField(max_length=2500, null=True, blank=True, help_text="Description of the server")
    hardware_vendor = models.ForeignKey(Vendors, related_name="servers")
    serial_number = models.CharField(max_length=150, null=True, help_text="Serial number")


class CiOperatingSystem(ConfigurationItem):
    """
    Operacios rendszerekre vonatkozo specifikus adatok
    """
    os_type = models.CharField(max_length=150)
    major_version = models.CharField(max_length=20)
    minor_version = models.CharField(max_length=20)
    network_interfaces = models.ForeignKey(IpAddress)
    hostname = models.CharField(max_length=250, null=True, help_text="Hostname known by the server")


class MiddlewareType(abstract_models.ActiveFieldModelAbstract):
    name = models.CharField(max_length=15, null=True)


class CiMiddlewareInstallation(ConfigurationItem):
    """
    Middleware installaciok
    """
    mdlw_type = models.ForeignKey(MiddlewareType)
    version = models.CharField(max_length=15, null=True, help_text="Version number of the middleware.")
    patch_level = models.CharField(max_length=15, null=True, help_text="Patch level of the middleware.")
    installation_path = models.CharField(max_length=200, null=True, help_text="Utvonal")
    description = models.TextField(max_length=500, null=True, help_text="Leiras")


class CiMiddlewareInstance(ConfigurationItem):
    """
    MIddleware Alkalmazasok
    """
    OBJECT_TYPES = (
        (1, "High"),
        (2, "Medium"),
        (3, "Low"),
    )

    admi_user = models.CharField(max_length=25, null=False, help_text="Admin felhasznalonev")
    category = models.IntegerField(choices=OBJECT_TYPES, default=3, help_text="Kategoria")
    comment = models.TextField(max_length=500, null=True, help_text="Comment")


class CiApplication(ConfigurationItem):
    name = models.CharField(max_length=50, null=True, help_text="Applikacio neve")
    vendor = models.ForeignKey(Vendors, related_name="applications")
    release = models.CharField(max_length=30)
    customer_evironment = models.CharField(max_length=30)


class Companies(abstract_models.ActiveFieldModelAbstract):
    name = models.CharField(max_length=30, null=True)
    contact_name = models.CharField(max_length=30, null=True)
    contact_email = models.EmailField(max_length=30, null=True)
    contact_phone = models.CharField(max_length=15, null=True)


class CiBusinessContract(ConfigurationItem):
    """
    Az alkalmazasokat osszefogo uzleti szerzodesek
    """
    OBJECT_TYPES = (
        (1, "High"),
        (2, "Medium"),
        (3, "Low"),
    )

    company = models.ForeignKey(Companies, null=True, help_text="Company", related_name="related_bc")
    availability = models.CharField(max_length=5, null=True)
    maintenance_window = models.CharField(max_length=30, null=True)
    severity = models.IntegerField(choices=OBJECT_TYPES, default=3, help_text="A rendelkezesre allas prioritasa")
    primary_mgmt_contact = models.ForeignKey(ManagerProfile, related_name="pri_contact_for")
    mgmt_group = models.ManyToManyField(ManagementGroups, related_name="managed_bc")
