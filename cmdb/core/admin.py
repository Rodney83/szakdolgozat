from django.contrib import admin
from django.contrib.auth.models import User
import models

admin.site.unregister(User)
admin.site.register(models.TechnicalGroups)
admin.site.register(models.ManagementGroups)
admin.site.register(models.UserProfile)
admin.site.register(models.ManagerProfile)
