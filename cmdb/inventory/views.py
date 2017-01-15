from django.shortcuts import render
from cmdb.prototypes import viewsets
import models
import serializers


class CiViewSet(viewsets.ModelViewSet):
    queryset = models.ConfigurationItem.objects.all()
    serializer_class = serializers.ConfigurationItemSerializer


class CiRelationViewSet(viewsets.CreateDestroyRetrieveViewSet):
    queryset = models.CiRelation.objects.all()
    serializer_class = serializers.CiRelationSerializer
