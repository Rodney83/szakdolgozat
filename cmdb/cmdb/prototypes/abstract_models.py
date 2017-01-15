from django.db import models

from cmdb.prototypes.model_magaers import ActiveFieldManager


class ActiveFieldModelAbstract(models.Model):
    """
    Absztrakt model osztaly amely rendelkezik egy aktive mezovel, es egy hozza tartozo managerrel
    """
    name = None
    active = models.BooleanField(default=True)

    everything = models.Manager()
    objects = ActiveFieldManager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name