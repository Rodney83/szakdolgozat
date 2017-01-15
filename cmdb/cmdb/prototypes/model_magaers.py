from django.db import models


class ActiveFieldManager(models.Manager):

    def get_queryset(self):
        return super(ActiveFieldManager, self).get_queryset().filter(active=True)
