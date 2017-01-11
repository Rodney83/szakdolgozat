from django.contrib import admin
import models


admin.site.register(models.TaskStatus)
admin.site.register(models.ChangeState)
admin.site.register(models.ClosureCode)
admin.site.register(models.Change)
admin.site.register(models.Task)