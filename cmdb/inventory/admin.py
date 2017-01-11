from django.contrib import admin
import models
# Register your models here.

admin.site.register(models.CiStatus)
admin.site.register(models.CiType)
admin.site.register(models.ConfigurationItem)
admin.site.register(models.CiRelation)
admin.site.register(models.Vendors)
admin.site.register(models.IpAddress)
admin.site.register(models.CiNetworkNode)
admin.site.register(models.CiServerNode)
admin.site.register(models.CiOperatingSystem)
admin.site.register(models.MiddlewareType)
admin.site.register(models.CiMiddlewareInstallation)
admin.site.register(models.CiMiddlewareInstance)
admin.site.register(models.CiApplication)
admin.site.register(models.Companies)
admin.site.register(models.CiBusinessContract)
