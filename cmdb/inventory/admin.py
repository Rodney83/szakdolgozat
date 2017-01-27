from django.contrib import admin
import models


class ConfigItemAdmin(admin.ModelAdmin):
    exclude = ('traverse_mark',)
    filter_horizontal = ('administrator_groups',)
    list_display = ('logical_name', 'verbose_name', 'ci_type', 'status')


class NetworkAdmin(ConfigItemAdmin):
    filter_horizontal = ConfigItemAdmin.filter_horizontal + ('ip_addresses',)


class OSAdmin(ConfigItemAdmin):
    filter_horizontal = ConfigItemAdmin.filter_horizontal + ('network_interfaces',)


class BCAdmin(ConfigItemAdmin):
    filter_horizontal = ConfigItemAdmin.filter_horizontal + ('mgmt_group',)


admin.site.register(models.CiStatus)
admin.site.register(models.CiType)
admin.site.register(models.ConfigurationItem, ConfigItemAdmin)
admin.site.register(models.CiRelation)
admin.site.register(models.Vendors)
admin.site.register(models.IpAddress)
admin.site.register(models.CiNetworkNode, NetworkAdmin)
admin.site.register(models.CiServerNode, ConfigItemAdmin)
admin.site.register(models.CiOperatingSystem, OSAdmin)
admin.site.register(models.MiddlewareType)
admin.site.register(models.CiMiddlewareInstallation, ConfigItemAdmin)
admin.site.register(models.CiMiddlewareInstance, ConfigItemAdmin)
admin.site.register(models.CiApplication, ConfigItemAdmin)
admin.site.register(models.Companies)
admin.site.register(models.CiBusinessContract, BCAdmin)
