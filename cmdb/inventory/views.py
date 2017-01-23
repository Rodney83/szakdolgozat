from cmdb.prototypes import viewsets
import models
import serializers


class InventoryRootView(viewsets.RootView):
    url_list = {
        'Configuration Items': 'configurationitem-list',
        'Network Noeds': 'cinetworknode-list',
        'Ci Status': 'cistatus-list',
        'Ci Types': 'citype-list',
        'Vendors': 'vendors-list',
        'IP Address': 'ipaddress-list',
        'Companies': 'companies-list',
    }


class CiViewSet(viewsets.ModelViewSet):
    queryset = models.ConfigurationItem.objects.all()
    serializer_class = serializers.ConfigurationItemDetailSerializer
    serializer_map = {
        'list': serializers.ConfigurationItemListSerializer
    }


class CiNetworkNodeViewset(viewsets.ModelViewSet):
    queryset = models.CiNetworkNode.objects.all()
    serializer_class = serializers.CiNetworkNodeDetailSerializer
    serializer_map = {
        'list': serializers.CiNetworkNodeListSerializer
    }


class CiRelationViewSet(viewsets.CreateDestroyRetrieveViewSet):
    queryset = models.CiRelation.objects.all()
    serializer_class = serializers.CiRelationSerializer


class CiStatusViewSet(viewsets.ModelViewSet):
    queryset = models.CiStatus.objects.all()
    serializer_class = serializers.CiStatusSerializer


class CiTypeViewSet(viewsets.ModelViewSet):
    queryset = models.CiType.objects.all()
    serializer_class = serializers.CiTypeSerializer


class VendorsViewSet(viewsets.ModelViewSet):
    queryset = models.Vendors.objects.all()
    serializer_class = serializers.VendorsSerializer
    serializer_map = {
        'list': serializers.VendorsSerializerMinimal
    }


class IpAddressViewSet(viewsets.ModelViewSet):
    queryset = models.IpAddress.objects.all()
    serializer_class = serializers.IpAddressSerializer


class CompaniesViewSet(viewsets.ModelViewSet):
    queryset = models.Companies.objects.all()
    serializer_class = serializers.CompaniesMinimalSerializer
    serializer_map = {
        'list': serializers.CompaniesMinimalSerializer
    }

