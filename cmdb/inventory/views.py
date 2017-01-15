from django.shortcuts import render
from cmdb.prototypes import viewsets
import models
import serializers


class CiListViewSet(viewsets.ListViewSet):
    queryset = models.ConfigurationItem.objects.all()
    serializer_class = serializers.ConfigurationItemListSerializer


class CiDetailViewSet(viewsets.CreateDestroyRetrieveUpdateViewSet):
    queryset = models.ConfigurationItem.objects.all()
    serializer_class = serializers.ConfigurationItemDetailSerializer


class CiRelationViewSet(viewsets.CreateDestroyRetrieveViewSet):
    queryset = models.CiRelation.objects.all()
    serializer_class = serializers.CiRelationSerializer
